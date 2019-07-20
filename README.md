To run the server:
$ FLASK_APP=api.py flask run

http://127.0.0.1:5000/

To make the flask server visible to the outside world, NGROK:
1. Install NGROK
1. Make sure local host server is running
1. Run `$ ./ngrok http 5000` from home directory

To trigger the Buildkite webhook and send a POST to this Flask app:
1. Copy `http://8585EXAMPLE8585.ngrok.io` from ngrok server
1. Paste that into buildkite.com -> select group -> settings -> notifications services -> Webhook (add if necessary) -> webhook url field (add a '/') at the end
1. Select `build.running` and `build.finished`
1. Select `Save Notification Settings`
1. Submit Github PR and merge. The merge will trigger a Buildkite Heroku build. The Buildkite Heroku build will trigger a webhook to this Flask app.
