import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
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


@app.route('/', methods=['GET'])
def home():
    # Always show links for 0,1,2,3
    links = "".join([
        f'<li><a href="/api/v1/resources/books/{i}">Book {i}</a></li>' for i in range(4)
    ])
    return f"""
    <h1>Distant Reading Archive</h1>
    <p>A prototype API for distant reading of science fiction novels.</p>
    <ul>{links}</ul>
    """


@app.route('/api/v1/resources/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    # If book_id is in range of books, return the book, else return []
    if 0 <= book_id < len(books):
        return jsonify(books[book_id])
    else:
        return jsonify([])

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

if __name__ == '__main__':
    app.run()