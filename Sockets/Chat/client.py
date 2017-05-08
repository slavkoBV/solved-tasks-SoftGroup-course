from socket import *
import sys
import select

host = 'localhost'
port = 5000

sock = socket(AF_INET, SOCK_STREAM)
try:
    sock.connect((host, port))
except sock.error:
    print('Unable to connect')
    sys.exit()

while True:
    connections = [sys.stdin, sock]

    read_sock, write_sock, error_sock = select.select(connections, [], [], 1)

    for s in read_sock:
        if s == sock:
            data = sock.recv(1024).decode()
            if not data:
                print('Server closed')
                sys.exit()
            else:
                sys.stdout.write(data)
                sys.stdout.write('[Me]: ')
                sys.stdout.flush()
        else:
            message = sys.stdin.readline()
            sock.send(message.encode())
            sys.stdout.flush()
