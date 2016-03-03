import random

def intro():
    print("Welcome to mystery-word, please select difficulty level.")
    print("[E]asy: 4-6 characters, [N]ormal: 6-10, [Hard]: 10+", sep="\n")
    option = ''
    while option not in ["ENH"]:
        option = input("--> ").upper()
    return option


def select_word(option):
    with open("/usr/share/dict/words") as words:
        word_list = words.read().split("\n")

    word_lengths = {"E": range(4, 7), "N": range(6, 11), "H": range(10, 100)}
    possible_words = [x for x in word_list if len(x) in word_lengths[option]]
    return random.choice(possible_words)


def display(guesses, word_image):




# Display: Guesses remaining, word image

# User guess function: valid input, check word and guess history, update guesses













