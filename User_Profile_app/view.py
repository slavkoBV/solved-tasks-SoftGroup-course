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
    response = '<h1>Wrong user</h1>'.encode()
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        request = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True)
        username = request['username'].value
        password = request['password'].value
        all_users = User.get_all_users(DB_FILE)
        if all_users:
            for user in all_users:
                if username in user:
                    if server_auth(password, user[2]):
                        action = '/update_profile'
                        html = open('template.html', 'r').read().format(user[1], user[3], user[4], action, user[5], user[6])
                        response = html.encode()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [response]


def update_profile(environ, start_response):
    response = '<h1>Update</h1>'.encode()
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    return [response]
