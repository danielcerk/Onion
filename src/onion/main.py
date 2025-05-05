from app import Onion

app = Onion()

def home(request, response):

    response.text = 'Hello, World!'

def contact(request, response):

    response.text = 'Email: danielcerqueira2346@gmail.com'

app.register('/index', home)
app.register('/contact', contact)

for path, handler in app.routes.items():

    app.add_route(path, handler)

if __name__ == '__main__':

    app.runner(app, 5000)
