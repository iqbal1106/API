import flask
from flask import Flask

wapp = flask.Flask(__name__)
wapp.config["DEBUG"] = True

@wapp.route('/')
@wapp.route('/index')
def index():
    user = {'username': 'IQBAL', 'sex': 'Male'}
    return '''
<html>
    <head>
        <title>Home Page - Iqbal's Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
        <h2> Your sex is '''+ user['sex'] + '''</h2>
    </body>
</html>'''

wapp.run()