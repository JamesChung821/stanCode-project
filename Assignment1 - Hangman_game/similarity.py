"""
File: similarity
Name: James Chung
------------------
This program is to find out a lost segment of DNA sequence
"""


def main():
    dna = input('Please give me a DNA sequence to search: ')
    match = input('What DNA sequence would you like to match? ')
    dna = dna.upper()
    match = match.upper()
    print(compare(dna, match))


def compare(dna, match):
    """
    This method is to find out the most similar part of DNA sequence
    :param dna: str, long sequence
    :param match: str, short sequence
    :return: str,
    """

    # Set variables
    a = 0
    max = 0
    b = 0
    # The number of times for the comparison of DNA sequence
    for i in range(len(dna)-len(match)+1):
        # The number of times for the comparison of each character in the DNA sequence
        for j in range(len(match)):
            if match[j] == dna[i+j]:
                # Record a number if the character is the same
                a += 1
        # Find out the most similar DNA sequence
        if a > max:
            max = a
            # Record the DNA sequence with maximum similarity
            b = i
        a = 0
    # Return the most similar part of DNA sequence
    return dna[b:b+len(match)]


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
