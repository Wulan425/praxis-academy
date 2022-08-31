from ast import Delete
from asyncore import read
from re import template
from turtle import update
from urllib import request
from venv import create
from flask import Flask, url_for 
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    return template("index.html")

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<user_name>')
def profile(user_name):
    return '{}\'s profile'.format(escape(user_name))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', user_name='John Doe'))


if __name__ == "__main__":
    app.run()

...
# method yang kita gunakan
# create  = POST
# read    = GET
# update  = PUT
# Delete  = DELETE
...
