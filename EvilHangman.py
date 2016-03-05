import sys
import random
from Hangman import intro, player_input, display, player_guess, update_board

# Simple version looks good.
# Do a few more playthroughs, commit, then work on better version.as
# Better version: maybe run all combos of guess occurances.



def create_word_list(option):
    """
    Longest possible word for hard set is 15.
    :param option: Difficulty level.
    :return: List of words that are the correct length.
    """

    length_dict = {"E": range(4,7), "N": range(6, 11), "H": range(10, 16)}
    letter_len = random.choice(length_dict[option])

    with open("/usr/share/dict/words") as words:
        word_list = words.read().split("\n")
    return [x.upper() for x in word_list if len(x) == letter_len]


def shift_list(guess, board):
    # select and return a new word list.
    # update board if necessary
    pass




mode = intro()

word_list = create_word_list(mode)

word_len = len(word_list[0])

remaining_tries = 8
board = ["_"] * word_len
missed_guesses = []

print("The word is {} characters long".format(word_len))


while remaining_tries > 4:
    display(remaining_tries, board, missed_guesses)
    guess = player_guess(board, missed_guesses)  # Returns a valid letter guess
    missed_guesses.append(guess)
    remaining_tries -= 1

    print("Darn, that letter is not in the word")

    word_list = [x for x in word_list if guess not in x] # Better variable?


secret_word = random.choice(word_list).upper()

while remaining_tries > 0:

    display(remaining_tries, board, missed_guesses)
    guess = player_guess(board, missed_guesses)

    if guess in secret_word:
        print("", "Good guess!", sep="\n")
        board = update_board(guess, secret_word, board)
    else:
        remaining_tries -= 1
        missed_guesses.append(guess)

    if "_" not in board:
        print("", secret_word, "You win!", sep="\n")
        break

print("You are out of guesses. The word was {}.".format(secret_word))
