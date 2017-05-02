from wsgiref.simple_server import make_server

from User_Profile_app.handlers import home_handler, profile_handler, update_profile, delete
from User_Profile_app.utils import DB_FILE, create_db

routes = {
    '/': home_handler,
    '/profile': profile_handler,
    '/update_profile': update_profile,
    '/delete': delete,
}


class Application(object):
    def __init__(self, app_routes):
        self.routes = app_routes

    @staticmethod
    def not_found(environ, start_fn):
        start_fn('404 Not Found', [('Content-Type', 'text/plain')])
        return ['404 Not Found'.encode()]

    def __call__(self, environ, start_fn):
        handler = self.routes.get(environ.get('PATH_INFO')) or self.not_found
        return handler(environ, start_fn)


def server_run(application):
    server = make_server('localhost', 8000, application)
    print("Serving HTTP on port 8000...")
    server.serve_forever()


if __name__ == '__main__':
    # Create database
    create_db(DB_FILE)
    app = Application(routes)
    # Run server
    server_run(app)
