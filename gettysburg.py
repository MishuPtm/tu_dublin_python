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
import requests


# Returns text from a link if link contains plain text
def get_text_from_link(link):
    output = ""
    try:
        response = requests.get(link)

        if response.ok and response.headers['Content-Type'] == "text/plain":
            for line in response.text:
                output += line
            return output
        return None
    except:
        return None


def get_text_from_file(path):
    output = ""
    with open(path, "r") as file:
        for line in file:
            output += line
    return output


speech = get_text_from_link("http://193.1.33.31:88/pa1/gettysburg.tx")
stop_words = get_text_from_link("http://193.1.33.31:88/pa1/stopwords.tx")

# If links to not work using local files instead
if speech is None:
    print("Could not access the speech online, accessing local copy")
    speech = get_text_from_file("csfiles/gettysburg.txt")

if stop_words is None:
    print("Could not access the stop words online, accessing local copy")
    stop_words = get_text_from_file("csfiles/stop_words.txt")
stop_words = stop_words.lower().split(",")

# Making a copy of the speech to remove punctuation signs from
speech_without_punctuation = speech
for sign in string.punctuation:
    speech_without_punctuation = speech_without_punctuation.replace(sign, " ")
speech_without_punctuation = speech_without_punctuation.replace("  ", " ")


# Creating a dictionary to count unique words longer than 3 letters and not in the stop words list
counter = {}
for word in speech_without_punctuation.split(" "):
    word = word.lower().strip()
    if word not in stop_words and len(word) > 3:
        if word not in counter:
            counter[word] = 1
        else:
            counter[word] += 1


# Returns a list of most used words in descending order
def get_most_used(values=None, count=5):

    # Making a clone of the original values so we do not modify the input
    clone = dict(values)
    most_used_in_order = []

    for _ in range(count):
        current_max_word = ""
        current_max_value = 0

        for item, value in clone.items():
            if value > current_max_value:
                current_max_word = item
                current_max_value = value

        most_used_in_order.append(current_max_word)
        clone[current_max_word] = 0

    return most_used_in_order


print(f"The speech contains {len(speech_without_punctuation.split(' '))} words if we exclude the stop words")
print(f"There are {len(counter)} unique words in the speech")
print(f"Most popular words are: {get_most_used(counter, 10)}")
