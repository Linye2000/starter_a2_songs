"""SongCollection Class"""

import json
from song import Song

class SongCollection:
    # Constructor method to initialize a new SongCollection object
    def __init__(self):
        self.songs = []  # Initialize an empty list to store Song objects

    # Method to add a song to the collection
    def add_song(self, song):
        self.songs.append(song)  # Append the song to the songs list

    # Method to calculate the number of unlearned songs in the collection
    def get_number_of_unlearned_songs(self):
        # Returns the count of songs that are not marked as learned
        return sum(not song.is_learned for song in self.songs)

    # Method to calculate the number of learned songs in the collection
    def get_number_of_learned_songs(self):
        # Returns the count of songs that are marked as learned
        return sum(song.is_learned for song in self.songs)

    # Method to load songs from a JSON file
    def load_songs(self, filename):
        with open(filename, 'r') as file:  # Open the file for reading
            songs_data = json.load(file)  # Load the JSON data from the file
            for song_data in songs_data:  # Iterate over each song in the JSON data
                # Create a Song object and add it to the list
                song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
                self.songs.append(song)

    # Method to save the songs to a JSON file
    def save_songs(self, filename):
        songs_data = [song.to_dict() for song in self.songs]  # Convert each song to a dictionary
        with open(filename, 'w') as file:  # Open the file for writing
            json.dump(songs_data, file, indent=2)  # Write the song data to the file in JSON format

    # Method to sort the songs in the collection
    def sort(self, key):
        # Sort the songs based on a specified attribute, defaulting to title if the attribute is the same
        self.songs.sort(key=lambda song: (getattr(song, key), song.title))

    # Magic method to define the string representation of a SongCollection object
    def __str__(self):
        # Joining each song's string representation with a newline
        return "\n".join(str(song) for song in self.songs)