"""Tests for Song class"""

from song import Song

def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    default_song = Song()  # Creating a Song object with default values
    print(default_song)  # Printing the default song
    # Assertions to check if default values are as expected
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned  # 'is_learned' should be False by default

    # Test initial-value song
    print("\nTest initial-value song:")
    # Creating a Song object with specified values
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)  # Printing the initial-value song
    # Assertions to check if the values are set as expected
    assert initial_song.artist == "Powderfinger"
    assert initial_song.title == "My Happiness"
    assert initial_song.year == 1996
    assert initial_song.is_learned  # 'is_learned' should be True

    # Test mark_as_learned and mark_as_unlearned methods
    print("\nTest mark_as_learned and mark_as_unlearned methods:")
    # Creating a Song object with 'is_learned' set to False (default)
    unlearned_song = Song("Unlearned Song", "Unknown Artist", 2000)
    print(f"Before learning: {unlearned_song}")  # Printing the unlearned song
    assert not unlearned_song.is_learned  # Check if the song is not learned

    # Mark the song as learned
    unlearned_song.mark_as_learned()
    print(f"After learning: {unlearned_song}")  # Printing the song after learning
    assert unlearned_song.is_learned  # Check if the song is learned

    # Mark the song as unlearned
    unlearned_song.mark_as_unlearned()
    print(f"After unlearning: {unlearned_song}")  # Printing the song after unlearning
    assert not unlearned_song.is_learned  # Check if the song is not learned again


run_tests()