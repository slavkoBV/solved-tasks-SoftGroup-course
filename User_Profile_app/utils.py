import hmac
import sqlite3

SECRET_KEY = 'secret'

DB_FILE = 'users.db'


def hash_generate(user_pass):
    """Generate hash of user password

    :param user_pass: string
    :return: hash.digest()
    """
    user_hash = hmac.new(SECRET_KEY.encode(), user_pass.encode())
    return user_hash.digest()  # ця штука записується в базу даних


def server_auth(user_pass_input, user_pass_db):
    user_input_hash = hash_generate(user_pass_input)
    if hmac.compare_digest(user_input_hash, user_pass_db):
        return True
    else:
        return False


def create_db(DB_FILE):
    conn = sqlite3.connect(DB_FILE)
    curs = conn.cursor()
    curs.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,
                                        password BLOB, first_name TEXT, last_name TEXT, email TEXT, phone TEXT)""")
    curs.close()
    conn.close()
