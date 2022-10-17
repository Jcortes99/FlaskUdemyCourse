from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/otrafuncion')
def otrafuncion():
    return '<p>adios</p>'

@app.route('/products')
def products():
    return '''<li>Milk</li>
    <li>Rice</li>
    <li>Bread</li>
    '''

@app.route('/greedings/<name>')
def greeding(name):
    return '<h1>hello {}, greeding form flask</h1>'.format(name)

@app.route('/longitud/<lent>')
def long(lent):
    return '<h1>The long of the input is {}</h1>'.format(len(lent))

@app.route('/login/<user>/<passw>')
def login(user,passw):
    if(user == passw):
        return f'<h1>Welcome {user}!</h1>'
    else:
        return 'Error, username and password do not match!'

@app.route('/sum/<a>/<b>/')
def sumato(a,b):
    return 'La suma es: {}'.format(int(a)+int(b))

if __name__=='__main__':
    app.run()