from app import Onion

app = Onion()

def welcome(request):

    return '<h2>Olá, tudo bem?</h2>'

def home(request, name):

    return f'<h1>Olá, {name}</h1>'

def contact(request):

    return 'Email: danielcerqueira2346@gmail.com'

app.register('/', welcome)
app.register('/index/<name>', home)
app.register('/contact', contact)

if __name__ == '__main__':

    app.runner(5000)
