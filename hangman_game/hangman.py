"""
File: hangman.py
Name: 許景涵
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program will randomly come up with a vocabulary,
    and the user can pick either one of the 26 alphabets for a guess.
    If the alphabet you pick is in the vocabulary, this program will 
    show you the relative position(s) of the alphabet. If not, 
    you lose one guess.(You have N_TURNS guesses.)
    The game ends either you guess all the alphabets right(win) or used up all 7 guesses(lose.)
    """
    word = random_word()
    word_len = len(word)
    turn = N_TURNS                # The chances left for the player to guess
    dashed_ans = '-' * word_len   # Cover the answer with dashes('-')

    while turn > 0:               # The player has guesses left
        print('The word looks like: ' + dashed_ans)
        print('You have ' + str(turn) + ' guesses left.')
        guess_ch = input('Your guess: ').upper()

        if not guess_ch.isalpha() or len(guess_ch) != 1:  # Check if correct format
            print('Illegal format.')
        else:
            if guess_ch in word:                          # The word has the alphabet you guess
                new_dashed_ans = ''                       # Used to update the ans
                for i in range(word_len):                 # Get the index of input_ch
                    if guess_ch == word[i]:
                        new_dashed_ans += guess_ch        # Show all correct input_ch out
                    else:
                        new_dashed_ans += dashed_ans[i]   # Show dashes

                dashed_ans = new_dashed_ans               # Update dashed_ans
                print('You are correct!')

                if dashed_ans == word:                    # Guess the complete word, or if '-' not in dashed_ans:
                    print('You win!!')
                    print('The word was: ' + word)
                    return
            else:          # The word doesn't have the alphabet you guess
                turn -= 1
                print('There is no ' + guess_ch + '\'s in the word.')
    print('You are completely hung :(')   # No guess left
    print('The word was: ' + word)


def random_word():
    """
    To pick a random answer.
    return: str, the answer picked.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# ---  DO NOT EDIT THE CODE BELOW THIS LINE  --- #
if __name__ == '__main__':
    main()
