"""
Author: Ionut Petrescu
Date: 04.01.2019
Lab exercise 5
Music notation



class Song:
    song_nb = int()
    title = ""
    time_sig = ""
    key_sig = ""

    def __init__(self, unformatted_data):
        self.song_nb = int(unformatted_data.split("X:")[1].split("\n")[0])
        self.title = unformatted_data.split("T:")[1].split("\n")[0]
        self.time_sig = unformatted_data.split("M:")[1].split("\n")[0]
        self.key_sig = unformatted_data.split("K:")[1].split("\n")[0]

    def __str__(self):
        return f"{self.song_nb}...{self.title}... Time sig: {self.time_sig}... Key sig: {self.key_sig}"


songs = []
"""


def print_song(unformatted_data):
    song_nb = int()
    title = ""
    time_sig = ""
    key_sig = ""
    """
    unformatted_data contains all info for a specific song, i format it using split
    To identify the begining and the end of the information i actually use
    unformatted_data.split("X:")[1] to get a string that starts with the song number
    I then split it again using .split("\n") and access the item [0] so only the number is retrieved and not the rest 
    The process is repeated for every variable required
    [0] takes the value from the left of separator and [1] takes the value from the right
    """
    try:
        song_nb = int(unformatted_data.split("X:")[1].split("\n")[0])
        title = unformatted_data.split("T:")[1].split("\n")[0]
        time_sig = unformatted_data.split("M:")[1].split("\n")[0]
        key_sig = unformatted_data.split("K:")[1].split("\n")[0]
        print(f"{song_nb}...{title}... Time sig: {time_sig}... Key sig: {key_sig}")
    except IndexError:
        print("Incomplete song data")


with open("csfiles/hnr1(3).abc", "r") as file:
    song_data = ""
    # Reading every line of the file
    for line in file:
        if "X:" in line and song_data != "":    # if X: is in the line it means this is a new song, except for the first
            # songs.append(Song(song_data))       # this creates a song object and appends it to the list
            print_song(song_data)   # this calls the method and sends in the entire information of the song
            song_data = line    # this clears the old song data and replaces it with a new line from next song
        else:
            song_data += line   # keeps adding lines to the data

#for song in songs:
#    print(song)
