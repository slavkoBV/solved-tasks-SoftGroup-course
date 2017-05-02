import hmac
import sqlite3


# Secret key for hash generate password
SECRET_KEY = 'secret'

# Name of database file
DB_FILE = 'users.db'


def hash_generate(user_pass):
    """Generate hash of user password

    :param user_pass: string
    :return: hash.digest()
    """
    user_hash = hmac.new(SECRET_KEY.encode(), user_pass.encode())
    return user_hash.digest()  # ця штука записується в базу даних


def server_auth(user_pass_input, user_pass_db):
    """Check if user is authorised or not

    :param user_pass_input: user input password
    :param user_pass_db: user password from database
    :return: True or False
    """
    user_input_hash = hash_generate(user_pass_input)
    if hmac.compare_digest(user_input_hash, user_pass_db):
        return True
    else:
        return False


def create_db(db_file):
    """Create table users in database DB_FiLE

    :param db_file: name of database file (as global variable)
    :return: None
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    curs.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT,
                                        password BLOB, first_name TEXT, last_name TEXT, email TEXT, phone TEXT)""")
    curs.close()
    conn.close()
