import random
from Hangman import intro, display, player_guess, update_board


def create_word_list(option):
    """
    Longest possible word for hard mode is set at 15.
    Word length is chosen at random from the range in the chosen difficulty
    mode.
    :param option: Difficulty level.
    :return: List of words that are the correct length.
    """
    length_dict = {"E": range(4, 7), "N": range(6, 11), "H": range(10, 16)}
    letter_len = random.choice(length_dict[option])

    with open("/usr/share/dict/words") as words:
        word_list = words.read().split("\n")
    return [x.upper() for x in word_list if len(x) == letter_len]


def make_key(word, guess):
    """
    Creates a string of binary characters to represent where the guessed
    letter appears in the word.
    :return: A string of 1's and 0's.
    """
    return "".join(["1" if x == guess else "0" for x in word])


def partition_word_list(guess, word_list):
    """
    Sorts the word list into sub-lists based on the positions of the
    guessed letter.
    :param guess: A valid guessed letter.
    :param word_list: List of all possible words before accounting for guess.
    :return: The longest possible sub-list.
    """
    sub_lists = {}
    for word in word_list:
        word_key = make_key(word, guess)
        if word_key in sub_lists:
            sub_lists[word_key].append(word)
        else:
            sub_lists[word_key] = [word]
    return max(sub_lists.items(), key=lambda x: len(x[1]))[1]


if __name__ == '__main__':

    mode = intro()

    word_list = create_word_list(mode)

    word_len = len(word_list[0])

    remaining_tries = 8
    board = ["_"] * word_len
    missed_guesses = []

    print("The word is {} characters long".format(word_len))

    while remaining_tries > 0 and "_" in board:
        display(remaining_tries, board, missed_guesses)
        guess = player_guess(board, missed_guesses)
        word_list = partition_word_list(guess, word_list)

        # Pick a word to represent defined information. If only a single word
        # is possible, this represents secret_word like in the original.
        sample = word_list[0]

        if guess in sample:
            print("", "Good guess!", sep="\n")
            board = update_board(guess, sample, board)
        else:
            print("", "Darn, you guessed wrong.", sep="\n")
            missed_guesses.append(guess)
            remaining_tries -= 1

    if "_" not in board:
        print("", "".join(board), "You win!", sep="\n")
    else:
        teaser_word = random.choice(word_list)

        print("", "I'm sorry, you are out of guesses.", sep="\n")
        print("The word was {}!".format(teaser_word))
