from dataclasses import dataclass

@dataclass
class Track():
    def __init__(self, name, artist):
    	self.name=name
    	self.artist=artist

class MusicLibrary:
    def __init__(self):
        self.tracks=[]

    def add_track(self, name, artist):
    	self.tracks.append(Track(name, artist))

    def search_song_name(self, query):
        if not query or not isinstance(query,str):
            raise Exception("query invalid")

        return [item for item in self.tracks if item.name==query]

    def search_artist_name(self, query):
        if not query or not isinstance(query,str):
            raise Exception("query invalid")

        return [item for item in self.tracks if item.artist==query]
