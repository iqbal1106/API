import flask
from flask import Flask, render_template

wapp = flask.Flask(__name__)
wapp.config["DEBUG"] = True

@wapp.route('/')
@wapp.route('/index')
def index():
    user = {'username': 'IQBAL', 'profession': 'Product Manager'}
    title = list(user.keys())[1]
    return render_template('index.html',profession = title, user=user)

wapp.run()