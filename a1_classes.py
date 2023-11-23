"""Assignment1 Code"""

# Copy my first assignment to this file, commit, then update to use Song class
# Use SongCollection class

"""
Name: Jiaxiang Lin
Date started: 22/10/2023
GitHub URL: https://github.com/Linye2000/starter_a1_songs.git
"""

# Importing required classes from other files
from song import Song
from songcollection import SongCollection
import json

# Function to load songs from a JSON file into a SongCollection object
def load_songs(filename):
    song_collection = SongCollection()  # Creating a new SongCollection object
    with open(filename, 'r') as file:  # Opening the JSON file for reading
        songs_data = json.load(file)  # Loading the JSON data into a variable
        for song_data in songs_data:  # Iterating over each song in the JSON data
            # Creating a Song object with data from the JSON file
            song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
            song_collection.add_song(song)  # Adding the Song object to the SongCollection
    return song_collection  # Returning the populated SongCollection object

# Function to display all songs in the collection
def display_songs(song_collection):
    songs = song_collection.songs  # Getting the list of Song objects
    for i, song in enumerate(songs, 1):  # Iterating over the songs with index starting from 1
        # Determining the learned status of the song
        learned_status = 'learned' if song.is_learned else 'not learned'
        # Printing song details
        print(f"{i}. {song.title} by {song.artist} {song.year} ({learned_status})")

# Function to add a new song to the collection
def add_new_song(song_collection):
    title = input("Title: ")  # Taking song title as input
    artist = input("Artist: ")  # Taking artist name as input
    year = int(input("Year: "))  # Taking year as input and converting it to an integer
    song_collection.add_song(Song(title, artist, year))  # Adding the new song to the collection

# Function to mark a song as learned
def learn_song(song_collection):
    display_songs(song_collection)  # Displaying all songs
    song_number = int(input("Enter the number of the song to mark as learned: "))  # Taking the song number as input
    song_to_learn = song_collection.songs[song_number - 1]  # Fetching the song to learn
    song_to_learn.is_learned = True  # Marking the song as learned
    print(f"You have learned {song_to_learn.title}")  # Confirming the action to the user

# Function to save the song collection to a JSON file
def save_songs(song_collection, filename):
    songs_data = [song.to_dict() for song in song_collection.songs]  # Converting each song to a dictionary
    with open(filename, 'w') as file:  # Opening the file for writing
        json.dump(songs_data, file, indent=4)  # Writing the song data to the file in JSON format

# Main function to run the program
def main():
    song_collection = load_songs("songs.json")  # Loading songs from the file
    while True:  # Starting an infinite loop for the menu
        print_menu()  # Displaying the menu
        choice = input(">>> ").upper()  # Taking the user's choice as input
        if choice == "Q":  # Quitting the program
            save_songs(song_collection, "songs.json")  # Saving songs before quitting
            break
        elif choice == "D":  # Displaying songs
            display_songs(song_collection)
        elif choice == "A":  # Adding a new song
            add_new_song(song_collection)
        elif choice == "L":  # Learning a song
            learn_song(song_collection)
        else:  # Handling invalid options
            print("Invalid option")

# Function to print the menu options
def print_menu():
    print("Menu:")
    print("D - Display songs")
    print("A - Add a song")
    print("L - Learn a song")
    print("Q - Quit")

# Entry point of the program
if __name__ == "__main__":
    main()
