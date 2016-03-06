import random
import sys


def get_word_list(mode):
    words_list = []

    with open("/usr/share/dict/words") as file:
        lines = file.readlines()

    for line in lines:
        words = line.split()

        for word in words:
            word = word.lower()

            if 4 <= len(word) <= 6 and mode[0] == "e":
                words_list.append(word)
            elif 6 <= len(word) <= 10 and mode[0] == "n":
                words_list.append(word)
            elif len(word) >= 10 and mode[0] == "h":
                words_list.append(word)

    return words_list


def letter_guess(already_guessed):

    guessed_letter = input("Guess a letter: ")

    while guessed_letter.isalpha() and guessed_letter not in already_guessed:
        already_guessed.append(guessed_letter[0])
        return guessed_letter
    else:
        print("Input invalid.")


def blank_replacer(length, the_word, letter, board_arg):

    for i in range(length):
        if letter in the_word[i]:
            board_arg = board_arg[0:i] + \
                        board_arg[i].replace("_", letter) + board_arg[i+1:]

    return board_arg


def play_again(user_input, replay):
    while replay:
        user_input = input("Another round? Y/N ").lower()
        if user_input.isalpha() and user_input == "y":
            return replay
        else:
            sys.exit()

if __name__ == '__main__':

    play = True

    play_response = ''

    while play:

        mode_input = input('\tType your difficulty setting:\
    \n(E)ASY\t\t (N)ORMAL\t  (H)ARD\n').lower()

        guessed_letters = []

        word_list = get_word_list(mode_input)

        word = random.choice(word_list)

        word_length = len(word)

        board = "_" * word_length
        print("The word has {} letters.".format(word_length))

        user_guesses = 0

        guesses_allowed = int(word_length) + 2

        while user_guesses < guesses_allowed:

            print(board)
            user_letter = str(letter_guess(guessed_letters))

            if user_letter in str(word):
                board = blank_replacer(word_length, word, user_letter, board)
            elif user_letter not in str(word) and user_letter in guessed_letters:
                user_guesses += 1

            print("You have used {} / {} guesses."\
                  .format(user_guesses, guesses_allowed))

            if word == str(board):
                print("WINNER! The word was {}!!".format(word))
                play_again(play_response, play)
            elif user_guesses == guesses_allowed:
                print("Sorry. You loss. The word is {}.".format(word))
                play_again(play_response, play)
