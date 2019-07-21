from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import json
import sys
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

# A POST route to receive webhooks from Buildkite
@app.route('/', methods=['POST'])
def webhook_input():
    print("webhook"); sys.stdout.flush()
    if request.method == 'POST':
        print(request.get_json())
        requests.get(
            'http://localhost:3000/api/v1/webhooks_test',
            params=request.get_json()
        )
        # parse_response(request.json)
        # print("---------------")
        # print(parse_response(request.json))
        # print("---------------")
        # return request.json
    else:
        abort(400)

# webhook_input = {'event': 'build.finished', 'build': {'id': '07c1edd1-cea7-4acc-8310-437d246495c6', 'url': 'https://api.buildkite.com/v2/organizations/speakeasy-group/pipelines/speakeasy/builds/60', 'web_url': 'https://buildkite.com/speakeasy-group/speakeasy/builds/60', 'number': 60, 'state': 'passed', 'blocked': False, 'message': 'Merge pull request #29 from davehardy632/initialize_flask\n\nAdds line', 'commit': 'a0a1ee1ec41fa7832def1209c0f08342ca01811f', 'branch': 'master', 'tag': None, 'source': 'webhook', 'creator': {'id': '7bef7242-bcf9-419b-bf69-ec257b123b4c', 'name': 'James Cape', 'email': 'james.cape@gmail.com', 'avatar_url': 'https://www.gravatar.com/avatar/4b5532e8941a72ff1cd743b487dde4ed', 'created_at': '2019-07-19 13:36:01 UTC'}, 'created_at': '2019-07-20 23:34:07 UTC', 'scheduled_at': '2019-07-20 23:34:07 UTC', 'started_at': '2019-07-20 23:34:07 UTC', 'finished_at': '2019-07-20 23:34:40 UTC', 'meta_data': {'buildkite:git:commit': 'commit a0a1ee1ec41fa7832def1209c0f08342ca01811f\nMerge: 7130eed 4c9d2c6\nAuthor:     James Cape <james.cape@gmail.com>\nAuthorDate: Sat Jul 20 17:34:06 2019 -0600\nCommit:     GitHub <noreply@github.com>\nCommitDate: Sat Jul 20 17:34:06 2019 -0600\n\n    Merge pull request #29 from davehardy632/initialize_flask\n    \n    Adds line'}, 'pull_request': None}, 'pipeline': {'id': '2580a4bf-865e-4086-ad7f-ff745c5e84a5', 'url': 'https://api.buildkite.com/v2/organizations/speakeasy-group/pipelines/speakeasy', 'web_url': 'https://buildkite.com/speakeasy-group/speakeasy', 'name': 'speakeasy', 'description': None, 'slug': 'speakeasy', 'repository': 'https://github.com/davehardy632/SpeakEasy', 'branch_configuration': None, 'default_branch': 'master', 'skip_queued_branch_builds': False, 'skip_queued_branch_builds_filter': None, 'cancel_running_branch_builds': False, 'cancel_running_branch_builds_filter': None, 'provider': {'id': 'github', 'settings': {'trigger_mode': 'code', 'build_pull_requests': True, 'pull_request_branch_filter_enabled': False, 'skip_builds_for_existing_commits': False, 'skip_pull_request_builds_for_existing_commits': True, 'build_pull_request_forks': False, 'prefix_pull_request_fork_branch_names': True, 'build_tags': False, 'publish_commit_status': True, 'publish_commit_status_per_step': False, 'separate_pull_request_statuses': False, 'publish_blocked_as_pending': False, 'filter_enabled': False, 'repository': 'davehardy632/SpeakEasy'}, 'webhook_url': 'https://webhook.buildkite.com/deliver/5fd17e13ab0af98c2387ae9a27e2397243b86d91781411ea07'}, 'builds_url': 'https://api.buildkite.com/v2/organizations/speakeasy-group/pipelines/speakeasy/builds', 'badge_url': 'https://badge.buildkite.com/8ccee9e2dfed342713746fcdba7a4f8e241c9f47b41993e20c.svg', 'created_at': '2019-07-19 14:14:47 UTC', 'env': {}, 'scheduled_builds_count': 0, 'running_builds_count': 1, 'scheduled_jobs_count': 0, 'running_jobs_count': 1, 'waiting_jobs_count': 0, 'steps': [{'type': 'script', 'name': ':heroku: Deploy', 'command': 'heroku git:remote --app arrogant-loon-34609\r\ngit push heroku "$BUILDKITE_COMMIT":master', 'artifact_paths': '', 'branch_configuration': 'master', 'env': {}, 'timeout_in_minutes': None, 'agent_query_rules': [], 'concurrency': None, 'parallelism': None}]}, 'sender': {'id': '7bef7242-bcf9-419b-bf69-ec257b123b4c', 'name': 'James Cape'}}

# parsed = {'event': 'build.finished'}

# @app.route('localhost:3000/api/v1/webhooks_test', methods=['GET'])
# def parse_response(response):
#     r = json.loads(response)
#     print(r)
#     build_result = r['build']['id']
#     # return json.loads(webhook)
#     # return jsonify(r)
#     return jsonify(build_result)

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
    app.run(debug=True)
