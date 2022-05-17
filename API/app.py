from flask import Flask
from SpotifyAPI import SpotifyAPI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return 'Hello, world!'

@app.route('/current/', methods=['GET'])
def current_song():
    return SpotifyAPI().getCurrentSongJson()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)