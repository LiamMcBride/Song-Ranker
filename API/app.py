from re import sub
from flask import Flask, redirect, url_for, request
from SpotifyAPI import SpotifyAPI
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return 'Hello, world!'

@app.route('/current/', methods=['GET'])
def current_song():
    return SpotifyAPI().getCurrentSongJson()

# @cross_origin
@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method != 'GET':
        print("Request recieved")
        submission = request
        print(submission)
        return "Success", 200

    return "Failed"

if __name__ == '__main__':
    #app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(host='0.0.0.0', port=105, debug=True)
    #app.config['CORS_HEADERS'] = 'Content-Type'