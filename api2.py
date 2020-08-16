import flask
from flask import Flask, jsonify, request

app1 = flask.Flask(__name__)
app1.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app1.route('/', methods=['GET'])
def home():
    return '<h1>Welcome to my home page</h1>'

@app1.route('/book/all', methods=['GET'])
def allbooks():
    return jsonify(books)

@app1.route('/book', methods=['GET'])
def book_id():
   if 'id' in request.args:
       id = int(request.args['id'])
   else:
        return 'Provide id field in the URL'

   for book in books:
        if book['id'] == id:
            returnStr = 'The title of the book for the id =' + str(id) + ' is: <h1>' + book['title']+ '</h1>'
            return returnStr
        else:
            returnStr = "Book not found with id= " + str(id)
   return returnStr

app1.run()



