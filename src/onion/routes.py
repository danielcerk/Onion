class Route:

    def __init__(self):

        self.routes = {}

    def home_app_default(self, request, response):

        response.text = '<h1>Olá, bem-vindo ao Onion</h1>'

    def register(self, path, handler):

        if len(self.routes) == 0 and path != '/':

            self.routes['/'] = self.home_app_default

        self.routes[path] = handler

        return handler