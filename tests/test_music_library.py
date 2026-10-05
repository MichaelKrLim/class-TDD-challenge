from lib.music_library import *
import pytest

def test_adding_tracks():
    library = MusicLibrary()
    library.add_track("very early", "bill evans")
    library.add_track("billie jean", "michael jackson")

    seen = {}

    for track in library:
        seen.add(track)
    
    assert seen == set(Track("very early", "bill evans"),Track("billie jean", "michael jackson"))


