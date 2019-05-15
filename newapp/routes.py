from newapp import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World test test!"

@app.route('/index2')
def index2():
    user = {'username': 'Chok'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', insidehtmluser=user, insidehtmlpost=posts)