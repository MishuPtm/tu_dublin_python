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


# Returns text from a link if link contains plain text
def get_text_from_link(link):
    output = ""
    try:
        import requests
        response = requests.get(link, timeout=2)

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


def remove_punctuation(input_str):
    output = input_str
    for sign in string.punctuation:
        output = output.replace(sign, " ")
    output = output.replace("  ", " ")
    return output


# Creating a dictionary to count unique words longer than 3 letters and not in the stop words list
def count_unique_words(input_str, stop_words):
    counter = {}
    for word in remove_punctuation(input_str).split(" "):
        word = word.lower().strip()
        if word not in stop_words and len(word) > 3:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
    return counter


# Returns a list of most used words in descending order
def get_most_used(counter_dict=None, count=5):

    # Making a clone of the original values so we do not modify the input
    clone = dict(counter_dict)
    most_used_in_order = []
    # Making sure we are not trying to retrieve a list longer than the dictionary
    if count > len(clone):
        count = len(clone)

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


def main():
    speech = get_text_from_link("http://193.1.33.31:88/pa1/gettysburg.txt")
    stop_words = get_text_from_link("http://193.1.33.31:88/pa1/stopwords.txt")

    # If links do not work using local files instead
    if speech is None:
        print("Could not access the speech online, accessing local copy")
        speech = get_text_from_file("csfiles/gettysburg.txt")

    if stop_words is None:
        print("Could not access the stop words online, accessing local copy")
        stop_words = get_text_from_file("csfiles/stop_words.txt")

    stop_words = stop_words.lower().split(",")
    counter = count_unique_words(speech, stop_words)
    print(f"There are {len(counter)} unique words in the speech excluding stop words")
    print(f"Most popular words are: {get_most_used(counter, 10)}")


if __name__ == "__main__":
    main()
