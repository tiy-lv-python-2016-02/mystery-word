import random
import sys


# Write test file
# Error: multiple letter guesses count as a missed guess. Good idea for a test.


def intro():
    """
    Welcomes player to game and asks them to select a difficulty level.
    :return: Difficulty option.
    """
    print("Welcome to mystery-word, please select difficulty level.")
    print("Type 'exit' at any point to exit the game.")
    print(
          "",
          "[E]asy: 4-6 characters",
          "[N]ormal: 6-10 characters",
          "[H]ard: 10+ characters",
          sep="\n"
    )
    option = input("Please enter E, N, or H: ").upper()
    while option not in "ENH":
        if option == "EXIT":
            sys.exit()
        option = input("Please enter E, N, or H: ").upper()
    return option


def select_word(option):
    """
    Selects a random secret word of the appropriate length.
    :param option: Difficulty level determines word length.
    :return: A random word.
    """
    with open("/usr/share/dict/words") as words:
        word_list = words.read().split("\n")

    word_lengths = {"E": range(4, 7), "N": range(6, 11), "H": range(10, 100)}
    possible_words = [x for x in word_list if len(x) in word_lengths[option]]
    return random.choice(possible_words).upper()


def display(guesses, word_image, missed_guesses):
    """
    Display information at the start of each round.
    :param guesses: Number of remaining missed guesses.
    :param word_image: The missing and guessed letters.
    :param missed_guesses: Guessed letters that were not in the word.
    :return:
    """
    plural_dict = {True: "guesses", False: "guess"}

    print("", " ".join(word_image), sep="\n")
    print("You have {} {} remaining".format(guesses, plural_dict[guesses > 1]))
    print("You have guessed: {}".format(missed_guesses))


def player_input():
    """
    An invalid entry will repeat the prompt.
    :return: A single letter from user.
    """
    guess = ''
    while not guess.isalpha() or len(guess) != 1:
        guess = input("Please guess a letter: ").upper()
        if guess == "EXIT":
            sys.exit()
    return guess


def player_guess(board, missed_guesses):
    """
    Check to see if guess has been guessed previously.
    :return: A valid player guess.
    """
    guess = player_input()
    if guess in missed_guesses or guess in board:
        print("You already guessed that one!", "", sep="\n")
        return player_guess(board, missed_guesses)
    else:
        return guess


def update_board(guess, secret_word, board):
    """
    :return: The board updated with a correct guess.
    """
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            board[i] = guess
    return board


def next_game():
    """
    Prompts user to ask if they want to play another game.
    :return: Player input.
    """
    print("")
    next_game = input("Enter 'Y' to play again, any other key to exit: ")
    return next_game.upper() == "Y"


def game():
    """
    The main function. Call to run the game.
    :return: True if the user wishes to play again.
    """
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
            print("", secret_word, "You win!", sep="\n")
            return next_game()

    print("You are out of guesses. The word was {}.".format(secret_word))
    return next_game()


if __name__ == '__main__':

    new_game = True

    while new_game:
        new_game = game()











