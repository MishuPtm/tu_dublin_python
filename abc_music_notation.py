"""
Author: Ionut Petrescu
Date: 04.10.2019 Lab exercise 5
Music notation
"""


class Song:
    song_nb = int()
    title = ""
    time_sig = ""
    key_sig = ""

    def __init__(self, _song_nb, _title, _time_sig, _key_sig):
        self.song_nb = _song_nb
        self.title = _title
        self.time_sig = _time_sig
        self.key_sig = _key_sig

    """This is a class method that i use as an alternate constructor.
    I am using this instead of the __init__ as it allows me to protect against incomplete song data"""
    @classmethod
    def from_string(cls, unformatted_data):
        try:
            song_nb = int(unformatted_data.split("X:")[1].split("\n")[0])
            title = unformatted_data.split("T:")[1].split("\n")[0]
            time_sig = unformatted_data.split("M:")[1].split("\n")[0]
            key_sig = unformatted_data.split("K:")[1].split("\n")[0]
            return cls(song_nb, title, time_sig, key_sig)
        except IndexError:
            return None

    def __str__(self):
        return f"{self.song_nb}...{self.title}... Time sig: {self.time_sig}... Key sig: {self.key_sig}"


def main():
    songs = []
    with open("csfiles/hnr1(3).abc", "r") as file:
        song_data = ""
        for line in file:
            if "X:" in line and song_data != "":    # if X: is in the line it means this is a new song
                song = Song.from_string(song_data)   # Creates a song object if valid data is given
                if song:
                    songs.append(song)  # Checks to see if the object exists before appending it to the list
                song_data = line    # this clears the old song data and replaces it with a new line from next song
            else:
                song_data += line   # keeps adding lines to the data

    for song in songs:
        print(song)


if __name__ == "__main__":
    main()
