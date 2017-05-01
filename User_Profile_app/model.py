import sqlite3
import re
from .utils import hash_generate, DB_FILE


class User:
    def __init__(self):
        self._username = None
        self._password = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._phone = None

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

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        pattern = re.compile(r'[\w]+@[\w]+[.][\w]+')
        if re.findall(pattern, email)[0]:
            self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    def save(self, DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        curs = conn.cursor()
        curs.execute("INSERT INTO users (username, password, \
                      first_name, last_name, email, phone ) VALUES (?, ?, ?, ?, ?, ?)", [self.username,
                                                                     self.password,
                                                                     self.first_name,
                                                                     self.last_name,
                                                                     self.email,
                                                                     self.phone])
        conn.commit()
        curs.close()
        conn.close()

    def update(self, user_id):
        conn = sqlite3.connect(DB_FILE)
        curs = conn.cursor()
        curs.execute("SELECT * FROM users WHERE id={}".format(user_id))
        user = curs.fetchone()
        user_id = user[0]
        self._username = user[1]
        self._password = user[2]
        self._first_name = user[3]
        self._last_name = user[4]
        self._email = user[5]
        self._phone = user[6]
        curs.execute("UPDATE users SET username=?, password=?, first_name=?, last_name=?, email=?, phone=? \
                    WHERE id=?", [self._username,
                                  self._password,
                                  self._first_name,
                                  self._last_name,
                                  self._email,
                                  self._phone,
                                  user_id])
        conn.commit()
        curs.close()
        conn.close()

    def delete(self, DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        curs = conn.cursor()
        curs.execute("DELETE FROM users WHERE username='{}'".format(self.username))
        conn.commit()
        curs.close()
        conn.close()

    @staticmethod
    def get_all_users(DB_FILE):
        conn = sqlite3.connect(DB_FILE)
        curs = conn.cursor()
        curs.execute("SELECT * FROM users")
        users = curs.fetchall()
        curs.close()
        conn.close()
        return users
