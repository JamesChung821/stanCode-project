"""
File: Milestone1.py
-----------------------
This file is to test the code for 
babyname.py milestone 1

"""
import sys


def add_data_for_name(name_data, year, rank, name):
	d = name_data
	if name not in d:
		d[name] = {}
		d[name][year] = rank
	else:
		if year in d[name]:
			if rank < d[name][year]:
				d[name][year] = rank
		else:
			d[name][year] = rank

# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #

def test1():
	name_data = {'Kylie':{'2010':'57'}, 'Nick':{'2010':'37'}}
	add_data_for_name(name_data, '2010', '208', 'Kate')
	print('--------------------test1----------------------')
	print(str(name_data))
	print('-----------------------------------------------')


def test2():
	name_data = {'Kylie':{'2010':'57'}, 'Nick':{'2010':'37'}, 'Sammy': {'1990':'100'}}
	add_data_for_name(name_data, '1990', '200', 'Sammy')
	print('-------------------test2-----------------------')
	print(str(name_data))
	print('-----------------------------------------------')


def test3():
	name_data = {'Kylie':{'2010':'57'}, 'Nick':{'2010':'37'}}
	add_data_for_name(name_data, '2000', '104', 'Kylie')
	print('--------------------test3----------------------')
	print(str(name_data))
	print('-----------------------------------------------')


def test4():
	name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
	add_data_for_name(name_data, '2010', '208', 'Kate')
	add_data_for_name(name_data, '1990', '100', 'Sammy')
	add_data_for_name(name_data, '1990', '200', 'Sammy')
	add_data_for_name(name_data, '2000', '104', 'Kylie')
	print('--------------------test4----------------------')
	print(str(name_data))
	print('-----------------------------------------------')


def main():
	args = sys.argv[1:]
	if len(args) == 1 and args[0] == 'test1':
		test1()
	elif len(args) == 1 and args[0] == 'test2':
		test2()
	elif len(args) == 1 and args[0] == 'test3':
		test3()
	elif len(args) == 1 and args[0] == 'test4':
		test4()


if __name__ == "__main__":
	main()