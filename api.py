from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
import sys

app = Flask(__name__)
app.config["DEBUG"] = True

# A POST route to receive webhooks from Buildkite
@app.route('/', methods=['POST'])
def webhook():
    print("webhook"); sys.stdout.flush()
    if request.method == 'POST':
        print(request.json)
        return '', 200
    else:
        abort(400)

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

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

if __name__ == '__main__':
    app.run()
