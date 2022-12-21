"""
File: anagram.py
Name: James Chung
This program is to find the anagrams words for the word input by user
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
# Finding contains w/o has_prefix spends 83s and with has_prefix spends 62s
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_list = []                # This is a dictionary including all english words
final_list = []               # This list contains all found anagrams
start = 0                     # Restart the has_prefix function
new_d = {}                    # This dict contains any repeated character
multiple_dict = {}            # A dict for marking each character if the input word has repeated character


def main():
    """
    Let user give a word, finding all the words comprised of its character
    """
    print(f'Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)')
    read_dictionary()
    word = input('Find anagrams for: ').lower()
    global final_list, multiple_dict, new_d
    while word != EXIT:
        print('Searching...')
        find_anagrams(word)
        print(f'{len(final_list)} anagrams: {final_list}')
        word = input('Find anagrams for: ').lower()
        final_list = []      # Empty the list
        multiple_dict = {}   # Empty the dict
        new_d = {}           # Empty the dict


def read_dictionary():
    """
    Create a dictionary
    """
    with open(FILE, 'r') as f:
        for line in f:
            word_list.append(line.strip())


def find_anagrams(s):
    """
    The function is designed to check whether the word has repeated character, separating different words into two distinct recursion
    :param s: str, a word given by user
    """
    global new_d
    check_character(s)
    if len(new_d) < 1:                # If the input word has no any repeated character
        helper_function(s, '')
    else:                             # If the input word has repeated characters
        put_in_dict(s)
        helper_function2(s, '', '')


def helper_function(s, current_str):
    """
    This function is to find all the anagrams without any repeated character
    :param s: str, a word given by user
    :param current_str: str, a temporary str for adding any possible character
    """
    global start
    if len(current_str) == len(s):
        if current_str not in final_list and current_str in word_list:
            print(f'Found: {current_str}')
            print('Searching...')
            final_list.append(current_str)
    else:
        for ch in s:
            if ch in current_str:
                pass
            else:
                current_str += ch
                helper_function(s, current_str)
                current_str = current_str[:len(current_str) - 1]
                """
                # has_prefix function, leaving here to compare the speed of finding anagrams
                if has_prefix(current_str):
                    # current_str += ch
                    helper_function(s, current_str)
                    current_str = current_str[:len(current_str) - 1]
                else:
                    current_str = current_str[:len(current_str) - 1]
                    pass
                start = 0
                """



def helper_function2(s, mark_str, current_str):
    """
    This function is to find all the anagrams with repeated characters
    :param s: str, a word given by user
    :param current_str: str, a temporary str for adding any possible character
    """
    global start
    if len(current_str) == len(s):
        start = 0   # Restart the has_prefix function
        if current_str not in final_list and current_str in word_list:
            print(f'Found: {current_str}')
            print('Searching...')
            final_list.append(current_str)
            start = 0   # Restart the has_prefix function
    else:
        for mark in multiple_dict:  # Use the mark to do the recursion
            if str(mark) in mark_str:
                pass
            else:
                mark_str += str(mark)
                current_str += multiple_dict[mark]
                """
                # This code left here is used to compare the speed of finding anagrams without has_prefix function
                helper_function2(s, mark_str, current_str)
                mark_str = str(mark_str[:len(mark_str) - 1])
                current_str = current_str[:len(current_str) - 1]
                """
                if has_prefix(current_str):
                    helper_function2(s, mark_str, current_str)
                    mark_str = str(mark_str[:len(mark_str) - 1])
                    current_str = current_str[:len(current_str) - 1]
                else:
                    mark_str = str(mark_str[:len(mark_str) - 1])
                    current_str = current_str[:len(current_str) - 1]
                    pass
                start = 0   # Restart the has_prefix function


def check_character(s):
    """
    This function build up a dictionary including any repeated character
    :param s: str, a word given by user
    """
    d = {}
    for ch in s:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    global new_d
    for key in d:
        if d[key] > 1:  # If the given word has repeated characters
            new_d[key] = d[key]


def put_in_dict(s):
    """
    Create a dictionary to mark each character
    :param s: str, a word given by user
    """
    d = multiple_dict
    for i in range (len(s)):
        d[i] = s[i]


def has_prefix(sub_s):
    """
    This function reduces the finding times of all the anagrams
    :param sub_s: str, any segment of current str
    :return: boolean, True or False
    """
    global start
    for i in range(start, len(word_list)):
        if word_list[i].startswith(sub_s):
            start = i
            return True
    return False


if __name__ == '__main__':
    main()
