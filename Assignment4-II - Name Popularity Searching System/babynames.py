"""
SC101P Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
File: babynames.py
Name: James Chung
----------------------
This program regulates the name data
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    d = name_data
    # If the data is new
    if name not in d:
        d[name] = {}
        d[name][str(year)] = str(rank)
    # If the data exists, the data is inserted into the dictionary
    else:
        if str(year) in d[name]:
            if int(rank) < int(d[name][year]):
                d[name][str(year)] = str(rank)
        else:
            d[name][str(year)] = str(rank)


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        i = 0
        for line in f:
            word_list = line.split(',')
            # First line is the year
            if i == 0:
                year = word_list[0]
                year = year.strip() # You should clean the space here, too.
            # Put each item into the rank and name dictionary
            else:
                rank = word_list[0]
                name1 = word_list[1]
                name2 = word_list[2]
                rank = rank.strip()
                name1 = name1.strip()
                name2 = name2.strip()
                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)
            # From the second line, the list includes the rank and name
            i += 1


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
                                    :type target: str # I replace object with str.

    """
    """
    # Jerry's suggestions
    # You can change both name and target into lower case and compare them.
    names = []
    for name in name_data:
        name_lower = name.lower()
        target = target.lower()
        if target in name_lower:
            names.append(name)
    return names
    """

    target_upper_letter = ''
    target_lower_letter = ''
    # Make first character upper
    for i in range(len(target)):
        ch_upper = target[i]
        if i == 0:
            target_upper_letter += target[i].upper()
        else:
            target_upper_letter += ch_upper
    # Make first character lower
    for j in range(len(target)):
        ch_lower = target[j]
        if j == 0:
            target_lower_letter += target[j].lower()
        else:
            target_lower_letter += ch_lower
    # Make a list
    names = []
    for key in name_data:
        if target_upper_letter in key:
            names += [key]
        elif target_lower_letter in key:
            names += [key]
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
