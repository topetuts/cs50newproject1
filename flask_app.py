# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://tehmoddkzlacke:b57e55406fee784669a37421764a05cdba3bb09a81c5e769ddf158d193e5dd06@ec2-50-17-227-28.compute-1.amazonaws.com:5432/dflpf9ppj0j7v0")
db = scoped_session(sessionmaker(bind=engine))

@app.route('/')
def index():
    return 'Hello from Chok! flaskapp'


@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/register', methods=["POST"])
def register():
    username = request.form.get("Username")
    password = request.form.get("password")
    email = request.form.get("email")
    gender = request.form.get("gender")
    db.execute("INSERT INTO users (username,password,email,gender) VALUES (:username, :password, :email, :gender)", {"username": username, "password": password, "email": email, "gender": gender})
    db.commit()

    return 'Successful!'


@app.route('/display')
def display():
    display = db.execute("SELECT * FROM users")
    return display



