from wsgiref.simple_server import make_server

class Run:

    def __init__(self):

        self.application = None
        self.port = None

    def runner(self, application, port):

        port = port if port else 8000

        print(f'Run: http://127.0.0.1:{port}')

        with make_server('', port, application) as server:

            server.serve_forever()