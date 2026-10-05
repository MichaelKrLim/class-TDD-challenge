from lib.music_library import *
import pytest

def test_adding_tracks():
    library = MusicLibrary()
    library.add_track("very early", "bill evans")
    library.add_track("billie jean", "michael jackson")
    tracks=library.tracks
    assert tracks[0].artist == "bill evans"
    assert tracks[0].name == "very early"

def test_returning_empty_tracks():
    library=MusicLibrary()

    for track in library.tracks:
        assert False and "should be empty"

def test_exceptions():
    library=MusicLibrary()
    with pytest.raises(Exception) as e:
        found=library.search_song_name("")
    assert str(e.value)=="query invalid"

def test_exceptions():
    library=MusicLibrary()
    with pytest.raises(Exception) as e:
        found=library.search_song_name("")
    assert str(e.value)=="query invalid"

def test_search_song_name():
    library=MusicLibrary()
    library.add_track("very early", "bill evans")
    library.add_track("billie jean", "michael jackson")
    found=library.search_song_name("very early")
    assert found[0]==Track("very early", "bill evans")

def test_search_artist_name():
    library=MusicLibrary()
    library.add_track("very early", "bill evans")
    library.add_track("billie jean", "michael jackson")
    found=library.search_artist_name("michael jackson")
    assert found==[Track("bille jean", "michael jackson")]
