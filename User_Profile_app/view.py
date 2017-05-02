import cgi

from User_Profile_app.model import User
from User_Profile_app.utils import DB_FILE, server_auth


def home_handler(environ, start_response):
    action = '/profile'
    html = open('login.html', 'r').read().format(action)
    response = html.encode()
    response_headers = [('Content-Type', 'text/html')]
    start_response('200 OK', response_headers)
    return [response]


def profile_handler(environ, start_response):
    response = ''.encode()
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        request = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True)
        username = request['username'].value
        password = request['password'].value
        user_db = User().get_user_by_username(username, DB_FILE)

        # Check if user exists
        if user_db:
            if server_auth(password, user_db[2]):
                action = '/update_profile'
                html = open('template.html', 'r').read().format(user_db[1], user_db[3],
                                                                user_db[4], action, user_db[5], user_db[6])
                response = html.encode()
            else:
                html = '<h1>Wrong password</h1'
                response = html.encode()
        else:
            # If user does not exist, register new user by username and password
            # later user can fill all fields of his profile
            user = User()
            try:
                user.username = username
                user.password = password
                user.save(DB_FILE)
                action = '/update_profile'
                html = open('template.html', 'r').read().format(user.username, user.first_name,
                                                                user.last_name, action, user.email, user.phone)

            except ValueError as err:
                html = '<h1>{}</h1>'.format(err)
            response = html.encode()
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [response]


def update_profile(environ, start_response):
    response = '<h1>Update</h1>'.encode()
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return [response]
