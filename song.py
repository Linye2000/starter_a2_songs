"""Song Class"""

# 2DO: Create your Song class in this file

class Song:
    def __init__(self, title="", artist="", year=0, is_learned=False):
        """Constructor for the Song class."""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_learned = is_learned

    def __str__(self):
        """String representation of the Song object."""
        return f"{self.title} by {self.artist}, Released: {self.year}, Learned: {self.is_learned}"

    def mark_as_learned(self):
        """Record the song as learned."""
        self.is_learned = True

    def mark_as_unlearned(self):
        """Record the song as unlearned."""
        self.is_learned = False

    def to_dict(self):
        """Return a dictionary with the song's properties."""
        return {
            'title': self.title,
            'artist': self.artist,
            'year': self.year,
            'is_learned': self.is_learned
        }