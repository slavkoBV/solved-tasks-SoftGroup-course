import sqlite3
import hmac

# Secret key for hash generate password
SECRET_KEY = 'secret'


def hash_generate(user_pass):
    """Generate hash of user password

    :param user_pass: string
    :return: hash.digest()
    """
    user_hash = hmac.new(SECRET_KEY.encode(), user_pass.encode())
    return user_hash.digest()


def check_password(user_pass_input, user_pass_db):
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


def create_user_db(db_file):
    """Create table users in database DB_FiLE

    :param db_file: name of database file (as global variable)
    :return: None
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    curs.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password BLOB)")
    curs.close()
    conn.close()


def create_post_db(db_file):
    """Create table users in database DB_FiLE

    :param db_file: name of database file (as global variable)
    :return: None
    """
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    curs.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, post TEXT)")
    curs.close()
    conn.close()


def save_msg_db(user, message, db_file):
    conn = sqlite3.connect(db_file)
    curs = conn.cursor()
    curs.execute("INSERT INTO posts (username, post) VALUES (?, ?)", [user, message])
    conn.commit()
    curs.close()
    conn.close()


class User:
    def __init__(self):
        self._username = None
        self._password = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if len(username) >= 3:
            self._username = username
        else:
            raise ValueError('Username must be not less than 3 symbols')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        if len(password) > 6:
            self._password = hash_generate(password)
        else:
            raise ValueError('Password too short, must be 6 or more symbols')

    def save(self, db_file):
        conn = sqlite3.connect(db_file)
        curs = conn.cursor()
        curs.execute("INSERT INTO users (username, password) VALUES (?, ?)", [self.username, self.password])
        conn.commit()
        curs.close()
        conn.close()

    @staticmethod
    def delete(db_file, username):
        conn = sqlite3.connect(db_file)
        curs = conn.cursor()
        curs.execute("DELETE FROM users WHERE username='{}'".format(username))
        conn.commit()
        curs.close()
        conn.close()

    @staticmethod
    def get_user_by_username(username, db_file):
        conn = sqlite3.connect(db_file)
        curs = conn.cursor()
        curs.execute("SELECT * FROM users WHERE username='{}'".format(username))
        user = curs.fetchone()
        curs.close()
        conn.close()
        if user:
            return user
        else:
            return None
