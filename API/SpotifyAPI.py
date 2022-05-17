import spotipy
from spotipy.oauth2 import SpotifyOAuth
from SpotifySecret import CLIENT_ID, CLIENT_SECRET, REDIRECT_LINK
from urllib.request import urlopen
import json

class SpotifyAPI():
    def __init__(self):
        self.authorize()
    
    def authorize(self):
        self.scope = "user-read-currently-playing"
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret= CLIENT_SECRET, redirect_uri=REDIRECT_LINK, scope=self.scope))
    
    def getCurrentSongData(self):
        results = self.sp.current_user_playing_track()
        if str(results) == "None":
            return "No Song Playing", "None", "None"
        artist = results["item"]["artists"][0]['name']
        song = results["item"]['name']
        photoArt = results["item"]["album"]["images"][0]["url"]

        return song, artist, photoArt

    def getCurrentSongJson(self):
        results = self.sp.current_user_playing_track()
        if str(results) == "None":
            return "No Song Playing", "None", "None"
        artist = results["item"]["artists"][0]['name']
        song = results["item"]['name']
        photoArt = results["item"]["album"]["images"][0]["url"]

        
        # x = '{ "artist": "Joe", "song":"EDM", "art":"1234"}'
        x = {
            "artist": artist,
            "song": song,
            "art": photoArt
        }
        

        return json.dumps(x)

api = SpotifyAPI()

print(api.getCurrentSongData())