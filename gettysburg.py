"""
This is an exercise in file analysis. Fundamentally it is an exercise in the use of the basic collection objects in
Python such as strings, lists, tuples, dictionaries and sets.

We are going to use Abraham Lincoln's Gettysburg address of 1863, This is famous for many things, including for being a
short speech.

TASKS

We are going to do some simple analysis on this.
1. Count the number of words in the speech. We will exclude from our analysis a number of 'stop words', in our example
these will be the definite and indefinite articles and some personal pronouns.
2. Count the unique words in the collection produced by 1 above.
3. Count the number of occurrences of each word.

"""
import string


speech = ""
with open("csfiles/gettysburg.txt", "r") as file:
    for line in file:
        speech += line


stop_words = []
with open("csfiles/stop_words.txt", "r") as file:
    for line in file:
        stop_words.append(line.strip())


temp = speech
for sign in string.punctuation:
    temp = temp.replace(sign, " ")

temp = temp.replace("  ", " ")

counter = {}
for word in temp.split(" "):
    word = word.lower().strip()
    if word not in stop_words:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1

def get_most_used(values = None, count = 5):
    if values is None:
        values = {}
    else:
        values = values
    output = []
    max = 0
    temp = ()
    while len(output) < count:
        for item, value in values.items():
            if value > max:
                max = value
                temp = (key, value)

srt = sorted(counter.values())
print(srt)
print(f"The speech contains {len(temp.split(' '))} words if we exclude the stop words")
print(f"There are {len(counter)} unique words in the speech")
print("")
