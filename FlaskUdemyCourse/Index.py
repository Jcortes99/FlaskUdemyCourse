from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/dictionary')
def dictirionary():
    dic = {'Name':'Juan', 'Lastname':'Gomez', 'Country':'Colombia'}
    return render_template('Index.html', dictionary = dic)

@app.route('/loop')
def loops():
    people = ['Juan','Jairo','Albeiro','Kaiosama']
    return render_template('loop.html', people = people)

@app.route('/conditional/<user>/<passw>')
def condi(user, passw):
    return render_template('Conditional.html',name = user, passw = passw)

@

if __name__ == '__main__':
    app.run()