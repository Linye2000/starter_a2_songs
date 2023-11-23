"""Song Class"""

class Song:
    # Constructor method to initialize a new Song object
    def __init__(self, title="", artist="", year=0, is_learned=False):
        self.title = title  # Setting the song title
        self.artist = artist  # Setting the artist name
        self.year = year  # Setting the release year of the song
        self.is_learned = is_learned  # Boolean flag to track if the song has been learned

    # Magic method to define the string representation of a Song object
    def __str__(self):
        # Returning a formatted string with song details
        return f"{self.title} by {self.artist}, Released: {self.year}, Learned: {self.is_learned}"

    # Method to mark the song as learned
    def mark_as_learned(self):
        self.is_learned = True  # Setting the is_learned flag to True

    # Method to mark the song as not learned
    def mark_as_unlearned(self):
        self.is_learned = False  # Setting the is_learned flag to False

    # Method to convert the song object to a dictionary
    def to_dict(self):
        # Returning a dictionary representation of the song
        return {
            'title': self.title,  # Title of the song
            'artist': self.artist,  # Artist name
            'year': self.year,  # Release year
            'is_learned': self.is_learned  # Learned status
        }