"""
Name: Jiaxiang Lin
Date Started: 10/11/2023
Brief Project Description:
This project is a Kivy-based Python app for managing a personal song collection,
featuring options to add, sort, and track learning progress of songs.
GitHub URL: https://github.com/Linye2000/starter_a2_songs
"""
# Create my main program in this file, using the SongListApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from song import Song
from songcollection import SongCollection
import json

# Define the main application class, inheriting from Kivy's App class
class SongListApp(App):
    # StringProperty for status text, updates automatically in the GUI
    status_text = StringProperty('')
    # ObjectProperty for storing the song collection
    song_collection = ObjectProperty(SongCollection())
    # NumericProperties for tracking the count of learned and to-learn songs
    learned = NumericProperty(0)
    to_learn = NumericProperty(0)

    # Build the app UI from the KV file
    def build(self):
        self.song_collection = SongCollection()
        self.song_collection.load_songs('songs.json')
        # print("Loaded songs:", self.song_collection.songs)  # Verify that the song is loaded
        self.root = Builder.load_file('app.kv')
        self.update_song_list()
        return self.root

    # Load songs from a file and update the song list in the UI
    def load_songs(self, filename):
        self.song_collection.load_songs(filename)
        self.update_song_list()

    # Update the displayed list of songs
    def update_song_list(self):
        # Clear existing song widgets if any
        if self.root and hasattr(self.root.ids, 'songs_box'):
            self.root.ids.songs_box.clear_widgets()
        # Create and add a button for each song
        for song in self.song_collection.songs:
            button_color = (0, 2, 200, 1) if song.is_learned else (1, 1, 1, 1)  # Blue for learned, Grey otherwise
            button = Button(text=f'{song.title} by {song.artist} ({song.year})',
                            background_color=button_color,
                            on_release=self.toggle_learned)
            button.song = song  # Associate the song object with the button
            self.root.ids.songs_box.add_widget(button)
        self.update_status_text()

    # Add a new song based on user input
    def add_song(self):
        # Retrieve input values
        title = self.root.ids.title_input.text
        artist = self.root.ids.artist_input.text
        year_text = self.root.ids.year_input.text

        # Validate input values
        if not title or not artist or not year_text:
            self.status_text = "All fields must be completed"
            return

        try:
            year = int(year_text)
            if year <= 0:
                self.status_text = "Year must be > 0"
                return
        except ValueError:
            self.status_text = "Please enter a valid number"
            return

        # Add the song to the collection and update UI
        self.song_collection.add_song(Song(title, artist, year))
        self.update_song_list()
        self.clear_inputs()

    # Clear input fields in the UI
    def clear_inputs(self):
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.status_text = ""

    # Toggle the learned status of a song
    def toggle_learned(self, button_instance):
        song = button_instance.song
        song.is_learned = not song.is_learned
        self.update_song_list()

    # Update the status text with counts of learned and unlearned songs
    def update_status_text(self):
        self.learned = self.song_collection.get_number_of_learned_songs()
        self.to_learn = self.song_collection.get_number_of_unlearned_songs()

    # Save the current state of songs when the app is closed
    def on_stop(self):
        self.save_songs('songs.json')

    # Save songs to a file
    def save_songs(self, filename):
        with open(filename, 'w') as file:
            json.dump([song.to_dict() for song in self.song_collection.songs], file, indent=4)

    # Sort songs based on a selected attribute
    def sort_songs(self, sort_key):
        sort_key_mapping = {'Artist': 'artist', 'Title': 'title', 'Year': 'year', 'Learned': 'is_learned'}
        actual_sort_key = sort_key_mapping.get(sort_key)
        if actual_sort_key:
            self.song_collection.sort(actual_sort_key)
            self.update_song_list()

# Start the application
if __name__ == '__main__':
    SongListApp().run()