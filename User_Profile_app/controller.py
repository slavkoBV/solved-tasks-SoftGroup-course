from wsgiref.simple_server import make_server

from User_Profile_app.view import home_handler, profile_handler, update_profile

routes = {
    '/': home_handler,
    '/profile': profile_handler,
    '/update_profile': update_profile
}


class Application(object):
    def __init__(self, routes):
        self.routes = routes

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


app = Application(routes)
server_run(app)
