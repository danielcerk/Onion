class Route:

    def __init__(self):

        self.routes = {}

    def register(self, path, handler):

        self.routes[path] = handler

        return handler

    
    