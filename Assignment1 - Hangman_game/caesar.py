"""
File: caesar.py
Name: James Chung
-----------------
This program is to create a Caesar cipher to keep a secret
"""
# This is the original alphabet sequence
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    secret_number = int(input('Secret number: '))
    ciphered_string = input('What\'s the ciphered string? ')
    ciphered_string = ciphered_string.upper()

    print('The deciphered string is: ' + decipher(secret_number, ciphered_string))


def decipher(secret_number, ciphered_string):
    """
    :param secret_number: num, a number
    :param ciphered_string:  str, a word
    :return: str,
    ------------------------------------
    This method is to decipher a confidential message based on the secret number and ciphered string
    """
    # Create a new string for new alphabet
    new_alphabet = ''
    i = secret_number
    # Reorganize the alphabet to a new alphabet
    new_alphabet += ALPHABET[len(ALPHABET)-i:] + ALPHABET[:len(ALPHABET)-i]
    # Create a new string for deciphered string
    deciphered_string = ''
    # Compare the ciphered string with the old alphabet
    for ch in ciphered_string:
        # Make sure every character is an alphabet
        if ch.isalpha():
            # Find out the position of ciphered character in new alphabet
            num = new_alphabet.find(ch)
            # Record the character with the same position in the old alphabet
            deciphered_string += ALPHABET[num]
        # If the character is not an alphabet, keep the character
        else:
            deciphered_string += ch
    return deciphered_string



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
