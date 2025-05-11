from wsgiref.simple_server import make_server
from wsgiref.validate import validator

class Run:

    def __init__(self):

        pass

    def runner(self, application):

        validate_app = validator(application)

        def start(port=8000):

            print(f'Running on: http://127.0.0.1:{port} | ( Press CTRL+C to quit )')

            with make_server('127.0.0.1', port, validate_app) as server:

                server.serve_forever()
                
        return start