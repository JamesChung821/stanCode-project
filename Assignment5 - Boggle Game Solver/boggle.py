"""
File: boggle.py
Name: James Chung
----------------------------------------
This program is to find all anagrams in a 4X4 character chessboard
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
# Running boggle w/o has_prefix spends 15s and with has_prefix spends 17s
FILE = 'dictionary.txt'
word_list = []					# A English dictionary
tuple_dict = {}					# A coordination dict
mark_dict = {}					# A character dict
count = 0						# Count the number of found anagrams
start = 0						# Restart the has_prefix function
num1 = 0						# Record the x coordination of the character chessboard
num2 = 0						# Record the y coordination of the character chessboard
final_list = []					# A list contains all found anagrams


def main():
	"""
	This function let user give a 4X4 character chessboard
	"""
	global count
	read_dictionary()
	str1 = input('1 row of letters: ').lower()
	if str1[0].isalpha() and str1[1] == ' ' and str1[2].isalpha() and str1[3] == ' ' and str1[4].isalpha() and \
	str1[5] == ' ' and str1[6].isalpha():
		str2 = input('2 row of letters: ').lower()
		if str2[0].isalpha() and str2[1] == ' ' and str2[2].isalpha() and str2[3] == ' ' and str2[4].isalpha() and \
				str2[5] == ' ' and str2[6].isalpha():
			str3 = input('3 row of letters: ').lower()
			if str3[0].isalpha() and str3[1] == ' ' and str3[2].isalpha() and str3[3] == ' ' and str3[4].isalpha() and \
					str3[5] == ' ' and str3[6].isalpha():
				str4 = input('4 row of letters: ').lower()
				if str4[0].isalpha() and str4[1] == ' ' and str4[2].isalpha() and str4[3] == ' ' and str4[
					4].isalpha() and str4[5] == ' ' and str3[6].isalpha():
					put_in_dict(str1, str2, str3, str4)
					find_word('', '')						# To do the recursion
					print(f'There are {count} words in total.')
				else:
					print('Illegal input')
			else:
				print('Illegal input')
		else:
			print('Illegal input')
	else:
		print('Illegal input')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word_list.append(line.strip())


def put_in_dict(str1, str2, str3, str4):
	"""
	Create two dicts to organize the character chessboard, which is easy to do the recursion
	:param str1: str, the first row of letters
	:param str2: str, the second row of letters
	:param str3: str, the third row of letters
	:param str4: str, the fourth row of letters
	"""
	d = tuple_dict
	dict = mark_dict

	d[(0, 1)] = (str1[0], 'a')
	d[(2, 1)] = (str1[2], 'e')
	d[(4, 1)] = (str1[4], 'i')
	d[(6, 1)] = (str1[6], 'm')
	d[(0, 2)] = (str2[0], 'b')
	d[(2, 2)] = (str2[2], 'f')
	d[(4, 2)] = (str2[4], 'j')
	d[(6, 2)] = (str2[6], 'n')
	d[(0, 3)] = (str3[0], 'c')
	d[(2, 3)] = (str3[2], 'g')
	d[(4, 3)] = (str3[4], 'k')
	d[(6, 3)] = (str3[6], 'o')
	d[(0, 4)] = (str4[0], 'd')
	d[(2, 4)] = (str4[2], 'h')
	d[(4, 4)] = (str4[4], 'l')
	d[(6, 4)] = (str4[6], 'p')

	dict['a'] = (0, 1)
	dict['b'] = (0, 2)
	dict['c'] = (0, 3)
	dict['d'] = (0, 4)
	dict['e'] = (2, 1)
	dict['f'] = (2, 2)
	dict['g'] = (2, 3)
	dict['h'] = (2, 4)
	dict['i'] = (4, 1)
	dict['j'] = (4, 2)
	dict['k'] = (4, 3)
	dict['l'] = (4, 4)
	dict['m'] = (6, 1)
	dict['n'] = (6, 2)
	dict['o'] = (6, 3)
	dict['p'] = (6, 4)


def find_word(mark_str, current_str):
	global count, num1, num2, start
	d = tuple_dict
	dict = mark_dict
	reference_list = ['m', 'n', 'o']	# A reference list for finding the next initial letter
	if len(current_str) > 3:
		start = 0
		if current_str in word_list and current_str not in final_list:
			count += 1
			final_list.append(current_str)
			print(f'Found: "{current_str}"')
	else:
		for key in d:
			if d[key][1] not in mark_str and -2 <= int(key[0])-num1 <= 2 and -1 <= int(key[1])-num2 <= 1:
				mark_str += d[key][1]
				current_str += d[key][0]
				num1 = key[0]				# Record the x coordination
				num2 = key[1]				# Record the y coordination
				find_word(mark_str, current_str)	# Recursion
				# If the length of anagram str is larger than four, keeping searching-----------------------------------
				if len(mark_str) >= 4:
					for key in d:
						if d[key][1] not in mark_str and -2 <= int(key[0]) - num1 <= 2 and -1 <= int(key[1]) - num2 <= 1:
							mark_str += d[key][1]
							current_str += d[key][0]
							num1 = key[0]
							num2 = key[1]
							find_word(mark_str, current_str)
							if len(mark_str) == 1 and mark_str in reference_list:
								num1 = 0
								num2 = 3
							else:
								num1 = dict[mark_str[len(mark_str) - 2]][0]
								num2 = dict[mark_str[len(mark_str) - 2]][1]
							mark_str = mark_str[:len(mark_str) - 1]
							current_str = current_str[:len(current_str) - 1]
				# ------------------------------------------------------------------------------------------------------
				# find_word(mark_str, current_str)  # Recursion
				if len(mark_str) == 1 and mark_str in reference_list:
					num1 = 0	# Set a new initial x coordination to let for each loop start from the neighboring x
					num2 = 3	# Set a new initial y coordination to let for each loop start from the neighboring y
				else:
					num1 = dict[mark_str[len(mark_str) - 2]][0]
					num2 = dict[mark_str[len(mark_str) - 2]][1]
				mark_str = mark_str[:len(mark_str) - 1]
				current_str = current_str[:len(current_str) - 1]
				"""
				# The code left here is to compare the speed of finding anagrams with has_prefix
				if has_prefix(current_str):
					find_word(mark_str, current_str)
					if len(mark_str) == 4:
						for key in d:
							if d[key][1] not in mark_str and -2 <= int(key[0]) - num1 <= 2 and -1 <= int(
									key[1]) - num2 <= 1:
								mark_str += d[key][1]
								current_str += d[key][0]
								num1 = key[0]
								num2 = key[1]
								find_word(mark_str, current_str)
								if len(mark_str) == 1 and mark_str in reference_list:
									num1 = 0
									num2 = 3
								else:
									num1 = dict[mark_str[len(mark_str) - 2]][0]
									num2 = dict[mark_str[len(mark_str) - 2]][1]
								mark_str = mark_str[:len(mark_str) - 1]
								current_str = current_str[:len(current_str) - 1]
					if len(mark_str) == 1 and mark_str in reference_list:
						num1 = 0
						num2 = 3
					else:
						num1 = dict[mark_str[len(mark_str) - 2]][0]
						num2 = dict[mark_str[len(mark_str) - 2]][1]
					mark_str = mark_str[:len(mark_str) - 1]
					current_str = current_str[:len(current_str) - 1]
				else:
					if len(mark_str) == 1 and mark_str in reference_list:
						num1 = 0
						num2 = 3
					else:
						num1 = dict[mark_str[len(mark_str) - 2]][0]
						num2 = dict[mark_str[len(mark_str) - 2]][1]
					mark_str = mark_str[:len(mark_str) - 1]
					current_str = current_str[:len(current_str) - 1]
					pass
				start = 0
				"""
			else:
				pass


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global start
	for i in range(start, len(word_list)):
		if word_list[i].startswith(sub_s):
			start = i
			return True
	return False


if __name__ == '__main__':
	main()
