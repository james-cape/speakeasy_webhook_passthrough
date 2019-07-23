from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import json
import sys
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

# A POST route to receive/send webhooks from Buildkite to Rails Speakeasy
@app.route('/', methods=['POST'])
def webhook_input():
    print("webhook"); sys.stdout.flush()
    if request.method == 'POST':
        # print(request.get_json())

        requests.get(
            'https://dashboard.heroku.com/apps/arrogant-loon-34609/api/v1/webhooks_test',
            params={
                'build_status': request.get_json()['event'],
                'build_state': request.get_json()['build']['state'],
                'commit_messages': request.get_json()['build']['message'],
                'creator': request.get_json()['build']['creator']['name']
            }
        )
    else:
        abort(400)

if __name__ == '__main__':
    app.run(debug=True)
