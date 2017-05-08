from socket import *
import threading
import os

from model import *


DB_FILE = 'chat.db'

host = 'localhost'
port = 5000

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(5)
print('Server started on ', host, ':', port)

MEMBERS = {}


def client_handler(connection, address):
    connection.send('Welcome to chat\n'.encode())
    while True:
        user = MEMBERS.get(connection, 'anonim')
        if user == 'anonim':
            auth(connection)
            continue
        else:
            try:
                client_message = connection.recv(1024).decode().strip()
                if client_message == 'Bye' or client_message == '':
                    if connection in MEMBERS:
                        MEMBERS.pop(connection)
                        break
                else:
                    message_to_broadcast = '[{}]: '.format(user) + client_message + '\n'
                    save_msg_db(user, client_message, DB_FILE)
                    broadcast(message_to_broadcast.encode(), connection)
            except Exception as err:
                print(err)
                continue


def auth(connection):
    try:
        connection.send('Input username\n'.encode())
        try:
            username = connection.recv(1024).decode().strip()
            connection.send('Input password\n'.encode())
            password = connection.recv(1024).decode().strip()
            user_db = User().get_user_by_username(username, DB_FILE)
            if user_db is not None:
                if check_password(password, user_db[2]):
                    connection.send('Hello {}! You are logged\n'.format(username).encode())
                else:
                    connection.send('Wrong password\n'.encode())
                    return False
            else:
                # Register new user
                user_db = User()
                try:
                    user_db.username = username
                    user_db.password = password
                    user_db.save(DB_FILE)
                    confirm = 'Congratulate {}. You are signed in\n'.format(username)
                    connection.send(confirm.encode())
                except ValueError as err:
                    connection.send('{}'.format(err).encode())
                    return False
            MEMBERS[connection] = username
            return True
        except Exception as err:
            print(err)
            connection.send('You are not signed in\n'.encode())
            return False
    except connection.error:
        return False


def broadcast(message, connection):
    for conn in MEMBERS:
        user = MEMBERS[connection]
        if conn != connection and (user and MEMBERS[conn]) != 'anonim':
            try:
                conn.send(message)
            except Exception as err:
                print(err)
                conn.close()
                if connection in MEMBERS:
                    MEMBERS.pop(connection)


def dispatcher():
    while True:
        connection, address = sock.accept()
        MEMBERS[connection] = 'anonim'
        print('Server connected by', address)
        try:
            th = threading.Thread(target=client_handler, args=(connection, address))
            th.start()
        except Exception as err:
            print(err)
            connection.close()
            sock.close()


if not os.path.isfile(DB_FILE):
    create_user_db(DB_FILE)
    create_post_db(DB_FILE)
dispatcher()
