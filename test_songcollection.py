"""Tests for SongCollection class"""

from song import Song
from songcollection import SongCollection

def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    song_collection = SongCollection()
    print(song_collection)
    assert not song_collection.songs  # an empty list is considered False

    # Test loading songs
    print("Test loading songs:")
    song_collection.load_songs('songs.json')
    print(song_collection)
    assert song_collection.songs  # assuming file is non-empty, non-empty list is considered True

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)

    # Test sorting songs
    print("Test sorting - year:")
    song_collection.sort("year")
    print(song_collection)

    # 2DO: Add more sorting tests

    # Test sorting songs by artist
    print("Test sorting - artist:")
    song_collection.sort("artist")
    print(song_collection)

    # Test sorting songs by title
    print("Test sorting - title:")
    song_collection.sort("title")
    print(song_collection)

    # Test marking a song as unlearned
    print("Test marking a song as unlearned:")
    song_collection.songs[0].mark_as_unlearned()
    print(song_collection)

    # 2DO: Test saving songs (check file manually to see results)

    # Test saving songs
    print("Test saving songs:")
    song_collection.save_songs('songs.json')

    # 2DO: Add more tests, as appropriate, for each method

    # Test finding songs by artist
    print("Test finding songs by artist:")
    artist_search_result = song_collection.find_songs_by_artist("Powderfinger")
    print(artist_search_result)

    # Test finding songs by year
    print("Test finding songs by year:")
    year_search_result = song_collection.find_songs_by_year(1996)
    print(year_search_result)


run_tests()