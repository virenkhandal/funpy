import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, abort
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VideoGrant
from twilio.rest import Client

load_dotenv()
twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
twilio_api_key_sid = os.environ.get('TWILIO_API_KEY_SID')
twilio_api_key_secret = os.environ.get('TWILIO_API_KEY_SECRET')
twilio_client = Client(twilio_api_key_sid, twilio_api_key_secret,
                       twilio_account_sid)
import uuid
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def homepage():
    return render_template('index.html')


@app.route('/join_room', methods=["GET"])
def join_room():
    return render_template('join_room.html')

@app.route('/create_room', methods=["GET"])
def create_room():
    return render_template('create_room.html')

@app.route('/room', methods=['GET', 'POST'])
def enter_room():
    return render_template('room.html')
def login():
    username = request.get_json(force=True).get('username')
    if not username:
        abort(401)

    token = AccessToken(twilio_account_sid, twilio_api_key_sid,
                        twilio_api_key_secret, identity=username)
    token.add_grant(VideoGrant(room='My Room'))

    return {'token': token.to_jwt().decode()}


if __name__ == "__main__":
    app.run(debug=True)