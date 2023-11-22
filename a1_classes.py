"""A1 Classes Code"""
# 2DO: Copy your first assignment to this file, commit, then update to use Song class
# Use SongCollection class if you want to

"""
Name: Jiaxiang Lin
Date started: 22/10/2023
GitHub URL: https://github.com/Linye2000/starter_a1_songs.git
"""

from song import Song
from songcollection import SongCollection
import json

def load_songs(filename):
    """Load songs from a JSON file and return a SongCollection object. """
    song_collection = SongCollection()
    with open(filename, 'r') as file:
        songs_data = json.load(file)
        for song_data in songs_data:
            song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
            song_collection.add_song(song)
    return song_collection


def display_songs(song_collection):
    """Display all songs in the collection with their number, title, artist, year, and learned status."""
    songs = song_collection.songs
    for i, song in enumerate(songs, 1):
        learned_status = 'learned' if song.is_learned else 'not learned'
        print(f"{i}. {song.title} by {song.artist} {song.year} ({learned_status})")


def add_new_song(song_collection):
    """Prompt the user to add a new song to the collection."""
    title = input("Title: ")
    artist = input("Artist: ")
    year = int(input("Year: "))  # Assuming that the year input is always a valid integer here
    song_collection.add_song(Song(title, artist, year))


def learn_song(song_collection):
    """Record a song as learned based on user input."""
    display_songs(song_collection)
    song_number = int(input("Enter the number of the song to mark as learned: "))
    song_to_learn = song_collection.songs[song_number - 1]
    song_to_learn.is_learned = True
    print(f"You have learned {song_to_learn.title}")


def save_songs(song_collection, filename):
    """Save the songs in the collection to a JSON file."""
    songs_data = [song.to_dict() for song in song_collection.songs]  # Assumes the Song class has a to_dict method
    with open(filename, 'w') as file:
        json.dump(songs_data, file, indent=4)


def main():
    """Main function to run the song list manager."""
    song_collection = load_songs("songs.json")
    while True:
        print_menu()
        choice = input(">>> ").upper()
        if choice == "Q":
            save_songs(song_collection, "songs.json")
            break
        elif choice == "D":
            display_songs(song_collection)
        elif choice == "A":
            add_new_song(song_collection)
        elif choice == "C":
            learn_song(song_collection)
        else:
            print("Invalid option")


def print_menu():
    """Print the main menu options to the console."""
    print("Menu:")
    print("D - Display songs")
    print("A - Add a song")
    print("C - Complete a song")
    print("Q - Quit")


if __name__ == "__main__":
    main()