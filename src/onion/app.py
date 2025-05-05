from run import Run
from routes import Route

class Onion(Route, Run):

    def __init__(self):

        super().__init__()

    def add_route(self, path, handler):

        self.routes[path] = handler

        return handler

    def __call__(self, environ, start_response):

        path = environ.get('PATH_INFO', '/')
        handler = self.routes.get(path)

        status = '200 OK'
        headers = [('Content-Type', 'text/html; charset=utf-8')]

        if handler:

            start_response(status, headers)

            class Request:

                pass

            class Response:

                def __init__(self):

                    self.text = ''

            request = Request()
            response = Response()

            handler(request, response)

            return [response.text.encode()]
        
        else:

            start_response('404 Not Found', headers)

            return [b'404 Not Found']

    