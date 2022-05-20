from datetime import date
import sqlite3

class Database():
    def __init__(self):
        self.conn = sqlite3.connect("API/songs.db")
        self.cur = self.conn.cursor()
        


    def insertSong(self, name, artist, album, rating, feel):
        print("Adding Song")
        query = '''INSERT INTO song_rankings(name, artist, album, rating, feel) VALUES("{}", "{}", "{}", {}, "{}");'''
        query = query.format(name, artist, album, rating, feel)

        self.cur.execute(query)

    def findSong(self, name, artist):
        print("Searching For Song")
        query = '''SELECT name, artist FROM song_rankings WHERE name="{}" AND artist="{}"'''
        query = query.format(name, artist)

        self.cur.execute(query)
        rows = self.cur.fetchall()

        return len(rows) > 0

    def closeDatabase(self):
        self.conn.commit()
        self.conn.close()

# db = Database()

# db.insertSong("blah", "joe", "blah2", 3, "hype")