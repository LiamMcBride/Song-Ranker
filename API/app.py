from re import sub
from flask import Flask, redirect, url_for, request
from matplotlib.font_manager import json_load
from SpotifyAPI import SpotifyAPI
from flask_cors import CORS, cross_origin
import json
from Database import Database

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return 'Hello, world!'

@app.route('/current/', methods=['GET'])
def current_song():
    data = SpotifyAPI().getCurrentSongJson()

    db = Database()

    if db.findSong(data["song"], data["artist"]):
        data["ranked"] = True
    else:
        data["ranked"] = False
    
    db.closeDatabase()

    return json.dumps(data)

# @cross_origin
@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method != 'GET':
        print("Request recieved")
        submission = request.get_json(force=True)
        print(submission)
        
        db = Database()

        if not db.findSong(submission["song"], submission["artist"]):

            db.insertSong(
                submission["artist"],
                submission["song"],
                submission["album"],
                submission["rating"],
                submission["feeling"]
            )
        db.closeDatabase()

        return "Success", 200

    return "Failed"

if __name__ == '__main__':
    #app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(host='0.0.0.0', port=105, debug=True)
    #app.config['CORS_HEADERS'] = 'Content-Type'