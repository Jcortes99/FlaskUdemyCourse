from flask import Flask

app = Flask(__name__)

@app.route('/home')

def introduccion():
    return '<h1>Hola saludo desde flask</h1>'

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





if __name__=='__main__':
    app.run()