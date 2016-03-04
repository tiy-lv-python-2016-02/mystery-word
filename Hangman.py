import random
import sys

# Clear screen
# Clean up loop in game()

# Write docs
# Write test file
# Error: multiple letter guesses count as a missed guess. Good idea for a test.

def intro():
    print("Welcome to mystery-word, please select difficulty level.")
    print("Type 'exit' to exit the game")
    print("[E]asy: 4-6 characters, [N]ormal: 6-10, [H]ard: 10+", sep="\n")
    option = input("--> ").upper()
    while option not in "ENH":
        option = input("--> ").upper()
    return option


def select_word(option):
    with open("/usr/share/dict/words") as words:
        word_list = words.read().split("\n")

    word_lengths = {"E": range(4, 7), "N": range(6, 11), "H": range(10, 100)}
    possible_words = [x for x in word_list if len(x) in word_lengths[option]]
    return random.choice(possible_words).upper()


def display(guesses, word_image, missed_guesses):
    # word_image is a list of dashes and guessed letters
    plural_dict = {True: "guesses", False: "guess"}

    print("", " ".join(word_image), sep="\n")
    print("You have {} {} remaining".format(guesses, plural_dict[guesses > 1]))
    print("You have guessed: {}".format(missed_guesses))


def player_input():
    # return a valid letter guess from player
    guess = ''
    while not guess.isalpha() or len(guess) != 1:
        guess = input("Please guess a letter: ").upper()
        if guess == "EXIT":
            sys.exit()
    return guess


def player_guess(board, missed_guesses):
    # Gets and returns a valid player guess.

    # Might be better to combine into one list of previous guesses
    guess = player_input()
    if guess in missed_guesses or guess in board:
        print("You already guessed that one!", "", sep="\n")
        return player_guess(board, missed_guesses)
    else:
        return guess


def update_board(guess, secret_word, board):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            board[i] = guess
    return board


# Display: Guesses remaining, word image

# User guess function: valid input, check word and guess history, update guesses

def game():
    mode = intro()

    secret_word = select_word(mode)

    print("The word is {} characters long".format(len(secret_word)))

    remaining_tries = 8
    board = ["_"] * len(secret_word)
    missed_guesses = []

    while remaining_tries > 0:

        display(remaining_tries, board, missed_guesses)
        guess = player_guess(board, missed_guesses)

        if guess in secret_word:
            board = update_board(guess, secret_word, board)
        else:
            remaining_tries -= 1
            missed_guesses.append(guess)

        if "_" not in board:
            return print(secret_word, "You win!", sep="\n")

    return print("You are out of guesses. The word was {}.".format(secret_word))


if __name__ == '__main__':

    game()











