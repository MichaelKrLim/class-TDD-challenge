# class-TDD-challenge
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 1. Describe the Problem

Tracks - Song name, Artist name, date added
MusicLibrary - add (track), return Tracks(), search_artist(q), search_song_name(q), most_recent_song_added()

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Track:
    def __init__(self, song_name, artist):
        # parameters:
            # song_name: string
            # artist: string
        # initialise track including date added using datetime 
        # nothing to be returned 

class MusicLibray:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   Set a set for tracks
        pass # No code here yet

    def add_track(self, song_name, artist):
        # Parameters:
        #   song_name: string representing a single song
        #   artist: string for the artist
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def __iter__(self):
        # Returns:
        #   returning a range into the set instead of returning the whole set and exposing 
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def search_song_name(self, query):
        # Parameters:
        #   query: string - song_name that user gives 
        # Returns:
        #   return a track/tracks based on if query matches song name 
        #   Or if not in set return None
        #  Exceptions:
        #   If query is empty or wrong data type - raise exception
        # iterative through the set and find matches based on query
    def search_artist(self, query):
        # Parameters:
        #   query: string - artist that user gives 
        # Returns:
        #   return a track/tracks based on if query matches artist
        #   Or return None if not in track
        #  Exception:
        #    If query is empty or wrong data type - raise exception
        # iterative through the set and find matches based on query

    def most_recent_song(self):
        # parameters:
        #  None
        # Return
        #   The track that was most recently added 

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Adding a single track and viewing it
"""

library = MusicLibrary()
library.add("very early","bill evans")

for x in library:
    print(x) # print every track for us to view

"""
Add 2 tracks and view it and then query for song_name
"""
library = MusicLibrary()
library.add("very early","bill evans")
library.add("billie jean","michael jackson")

for x in library:
    print(x) # print every track for us to view

track = library.search_song_name("billie jean") #should return Track("billie jean", "michael jackson")

"""
Add 3 tracks, view it and query for artist but give empty artist query
"""
library = MusicLibrary()
library.add("very early","bill evans")
library.add("billie jean","michael jackson")
library.add("track3", "artist3")

for x in library:
    print(x) # print every track for us to view

try: 
    artist = library.search_artist("") #should return exception error that says "query is empty"
except: 
    print("success")
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._