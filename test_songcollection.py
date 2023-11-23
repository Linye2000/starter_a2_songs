"""Tests for SongCollection class"""

from song import Song
from songcollection import SongCollection

def run_tests():
    # Test case for an empty SongCollection
    print("Test empty SongCollection:")
    song_collection = SongCollection()  # Creating an empty SongCollection object
    print(song_collection)  # Displaying the empty collection
    assert not song_collection.songs  # Assert that the songs list is empty

    # Test case for loading songs from a file
    print("Test loading songs:")
    song_collection.load_songs('songs.json')  # Loading songs from a JSON file
    print(song_collection)  # Displaying the collection after loading songs
    assert song_collection.songs  # Assert that the collection is not empty after loading songs

    # Test case for adding a new song to the collection
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))  # Adding a new song
    print(song_collection)  # Displaying the collection after adding a song

    # Test cases for sorting the songs in different ways
    print("Test sorting - year:")
    song_collection.sort("year")  # Sorting songs by year
    print(song_collection)  # Displaying the collection after sorting by year

    # 2DO: Add more sorting tests

    # Test sorting songs by artist
    print("Test sorting - artist:")
    song_collection.sort("artist")  # Sorting songs by artist
    print(song_collection)  # Displaying the collection after sorting by artist

    # Test sorting songs by title
    print("Test sorting - title:")
    song_collection.sort("title")  # Sorting songs by title
    print(song_collection)  # Displaying the collection after sorting by title

    # Test case for marking a song as unlearned
    print("Test marking a song as unlearned:")
    song_collection.songs[0].mark_as_unlearned()  # Marking the first song as unlearned
    print(song_collection)  # Displaying the collection after marking a song as unlearned

    # 2DO: Test saving songs (check file manually to see results)

    # Test case for saving songs to a file
    print("Test saving songs:")
    song_collection.save_songs('songs.json')  # Saving the current state of the collection to a file

    # 2DO: Add more tests, as appropriate, for each method

    # Test cases for finding songs by a specific artist or year
    print("Test finding songs by artist:")
    artist_search_result = song_collection.find_songs_by_artist("Powderfinger")  # Finding songs by the artist "Powderfinger"
    print(artist_search_result)  # Displaying the result of the artist search

    # Test finding songs by year
    print("Test finding songs by year:")
    year_search_result = song_collection.find_songs_by_year(1996)  # Finding songs from the year 1996
    print(year_search_result)  # Displaying the result of the year search

run_tests()