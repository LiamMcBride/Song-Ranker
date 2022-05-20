from datetime import date
import sqlite3

class Database():
    def __init__(self):
        self.conn = sqlite3.connect("songs.db")
        self.cur = self.conn.cursor()
        


    def insertSong(self, name, artist, album, rating, feel):
        print(name + artist + album + str(rating) + feel)
        query = '''INSERT INTO song_rankings(name, artist, album, rating, feel) VALUES("{}", "{}", "{}", {}, "{}");'''
        query = query.format(name, artist, album, rating, feel)

        self.cur.execute(query)
        self.conn.commit()
        self.conn.close()

db = Database()

db.insertSong("blah", "joe", "blah2", 3, "hype")