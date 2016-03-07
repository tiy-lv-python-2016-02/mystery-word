import random

# create a list of words that could be used in the game.
file = open('/usr/share/dict/words')

wordlist = file.readlines()  # there are 235,886 lines

mystery_word = random.choice(wordlist).lower()
correct_guesses = []
wrong_guesses = []

if __name__ == '__main__':

    while True:
        play = input("\nDo you want to play Hangman? Type 'Yes'to begin.\n")
        if play.lower() != "yes":
            break

        # draw the lines for the mystery_word, including correct guesses and wrong guesses
        while len(wrong_guesses) < 8 and len(correct_guesses) != len(mystery_word):
            for letter in mystery_word:
                if letter in correct_guesses:
                    print(letter, end="")
                else:
                    print("_", end=" ")

            guess_letter = input("\nGuess a letter.\n").lower()

            # determine if guessed letter is correct
            if len(guess_letter)!= 1 or not guess_letter.isalpha():
                print("\n Please guess single letters only.\n")
            elif guess_letter in correct_guesses or guess_letter in wrong_guesses:
                print("\n Please guess a letter you have not already guessed.\n")
            elif guess_letter in mystery_word:
                correct_guesses.append(guess_letter)
                if len(correct_guesses) == len(list(mystery_word)):
                    print("\nGood work. You guessed {}, the mystery word.\n".format(mystery_word))
            else:
                wrong_guesses.append(guess_letter)

            print("You have made {} wrong guesses.\n".format(len(wrong_guesses)))
            print("You have {} guesses left.\n".format(8-len(wrong_guesses)))
            # I put these print statements on a separate lines bc I was tired of getting the message that my line was too long

        else:
            print("you didn't guess the mystery word, {}.".format(mystery_word))