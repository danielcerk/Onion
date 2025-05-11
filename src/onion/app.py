from run import Run
from routes import Route

from utils.request import Request

class Onion():

    def __init__(self):

        self.router = Route()
        self.register = self.router.register
        self.runner = Run().runner(self.__call__)

    def __call__(self, environ, start_response):

        args = ()
        kwargs = {}

        path = environ.get('PATH_INFO', '/')
        handler = self.router.routes.get(path)

        print(self.router.routes.items())

        status = '200 OK'
        headers = [('Content-Type', 'text/html; charset=utf-8')]

        if handler:

            start_response(status, headers)

            request = Request()

            result = handler(request, *args, **kwargs)

            if isinstance(result, str):

                result = result.encode('utf-8')

            return [result]
        
        else:

            start_response('404 Not Found', headers)

            return [b'404 Not Found']