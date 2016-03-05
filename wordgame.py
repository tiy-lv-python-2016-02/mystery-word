import random


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


def letter_guess(letter_guesses):

    guessed_letter = input("Guess a letter:")

    if guessed_letter.isalpha() and guessed_letter not in letter_guesses:
        letter_guesses.append(guessed_letter)
        return guessed_letter
    else:
        letter_guess(letter_guesses)


def blank_replacer(length, the_word, letter, board_arg):

    for i in range(length):
        if letter in the_word[i]:
            board_arg = board_arg[0:i] + \
                        board_arg[i].replace("_", letter) + board_arg[i+1:]

    return board_arg

if __name__ == '__main__':

    mode_input = input('\tType your difficulty setting:\
    \n(E)ASY\t\t (N)ORMAL\t  (H)ARD\n').lower()

    guessed_letters = []

    word_list = get_word_list(mode_input)

    word = random.choice(word_list)

    word_length = len(word)

    board = "_" * word_length

    guesses = word_length + 1

    while guesses != 0:

        user_letter = str(letter_guess(guessed_letters))

        if user_letter in str(word):
            board = blank_replacer(word_length, word, user_letter, board)
        elif user_letter in guessed_letters:
            guesses = guesses
        else:
            guesses -= 1

        print("You have {} guesses remaining.".format(guesses))

        if word == str(board):
            print("WINNER! The word was {}!!".format(word))
            break

        print(board)
