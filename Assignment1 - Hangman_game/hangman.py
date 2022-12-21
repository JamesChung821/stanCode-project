"""
File: hangman.py
Name: James Chung
-----------------
"""
import random

# The times of chances you can guess
N_TURNS = 7


def main():
    """
    This program is to guess a word and be hung if you guess wrong many times.
    """
    answer = random_word()  # A given answer
    a = N_TURNS  # Total turns
    # Start and explain
    print('The word looks like: ', end="")
    for i in range(len(answer)):
        print('-', end="")
    print('')
    print('Also, there are ' + str(len(answer)) + ' characters in the word.')
    print('You have ' + str(a) + ' guesses left.')
    input_ch = input('Your guess: ')
    input_ch = input_ch.upper()
    # Set two empty strings
    ans = ''
    fixed_ch = ''
    # An empty string with dashes
    for f in range(len(answer)):
        fixed_ch += ' '
    # Let's guess
    while a > 0:
        # Set an illegal format
        if not input_ch.isalpha() or len(input_ch) > 1:
            print('illegal format')
            input_ch = input('Your guess: ')
            input_ch = input_ch.upper()
        # Start to guess
        else:
            # You guess a character
            if answer.find(input_ch) != -1:
                j = 0
                # Whether the part of the word was guessed before
                for ch1 in fixed_ch:
                    # If a character was guessed before, keep it
                    if ch1.isalpha():
                        ans += ch1
                        j += 1
                    # If a character was not guessed before, keep going
                    else:
                        # If a character is guessed now, fill in
                        if input_ch == answer[j]:
                            ans += input_ch
                        # If your guess is wrong, fill in a dash
                        else:
                            ans += '-'
                        j += 1
                print('You are correct!')
            # If you did not guess a character
            else:
                # Whether the part of the word was guessed before
                for ch1 in fixed_ch:
                    # If a character was guessed before, keep it
                    if ch1.isalpha():
                        ans += ch1
                    # If a character was not guessed before, fill in a dash
                    else:
                        ans += '-'
                # Record your turns
                a -= 1
                print('There is no ' + input_ch + '\'s in the word.')
                # Hangman process
                if a > 0:
                    for i in range(16):
                        print('=', end="")
                    print('||')
                    for i in range(16):
                        print('=', end="")
                    print('||')
                    for k in range(2):
                        print('  ||      |')
                    if a == 6:
                        print('  ||     ( )')
                        for k1 in range(3):
                            print('  ||')
                    elif a == 5:
                        print('  ||     (O)')
                        for k1 in range(3):
                            print('  ||')
                    elif a == 4:
                        print('  ||     (O)')
                        print('  ||      |')
                        for k1 in range(2):
                            print('  ||')
                    elif a == 3:
                        print('  ||     (O)')
                        print('  ||      |\\')
                        for k1 in range(2):
                            print('  ||')
                    elif a == 2:
                        print('  ||     (O)')
                        print('  ||     /|\\')
                        for k1 in range(2):
                            print('  ||')
                    elif a == 1:
                        print('  ||     (O)')
                        print('  ||     /|\\')
                        print('  ||     /')
                        for k1 in range(1):
                            print('  ||')
                    for l in range(6):
                        print('=', end="")
                    print('')
            # Store the ans into a fixed-string
            fixed_ch = ans
            # If you guess the word
            if fixed_ch.isalpha():
                print('You win!!')
                break
            # If you have chances, please continue to guess
            if a > 0:
                print('The word looks like: ' + ans)
                print('You have ' + str(a) + ' guesses left.')
                ans = ''
                input_ch = input('Your guess: ')
                input_ch = input_ch.upper()
    # If you have no chance and do not guess the word, you are hung
    if a == 0:
        hangman()
        print('')
        print('You are completely hung : (')
    # The answer is...
    print('The word was: ' + answer)


def hangman():
    """
    A dead hangman
    """
    for i in range(16):
        print('=', end="")
    print('||')
    for i in range(16):
        print('=', end="")
    print('||')
    print('  ||      |')
    print('  ||     (O)')
    print('  ||     /|\\')
    print('  ||     / \\')
    print('  ||  you = dead')
    for l in range(6):
        print('=', end="")

def random_word():
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


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
