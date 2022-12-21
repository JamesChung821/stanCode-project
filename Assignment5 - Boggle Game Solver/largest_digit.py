"""
File: largest_digit.py
Name: James Chung
This program is to find the largest digit
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	Find the largest digit
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	A recursive function for comparing the digits
	:param n: int, several digits
	:return: int, the biggest digit
	"""
	# Confirm that the parameter is a positive number
	if n < 0:
		num = n*-1
	else:
		num = n
	# Base case, the first digit is compared
	if num//10 == 0:
		return num%10
	# Compare the digits, return the biggest one
	else:
		return max(num%10, find_largest_digit(num//10))



if __name__ == '__main__':
	main()
