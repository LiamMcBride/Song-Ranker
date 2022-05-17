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

@app.route('/submit/<rand>', methods=['POST'])
@cross_origin
def submit(rand):
    submission = request.json
    f = open("testFile.txt", "a")
    f.write(rand)
    f.close()

if __name__ == '__main__':
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(host='0.0.0.0', port=105)
    app.config['CORS_HEADERS'] = 'Content-Type'