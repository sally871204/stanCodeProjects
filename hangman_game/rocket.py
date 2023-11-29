"""
File: rocket.py
Name: 許景涵
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	head()
	belt()
	upper()
	lower()
	belt()


def head():
	for i in range(SIZE):
		for j in range(SIZE-i-1):
			print('', end='')
		for k in range(i+1):
			print('/', end='')
		print('\n', end='')
	for i in range(SIZE):
		for j in range(i+1):
			print('\\', end='')
		print('')


def belt():
	print('+', end='')
	print('=' *2*SIZE, end='')
	print('+')


def upper():
	for i in range(SIZE):
		for j in range(2*SIZE + 2):






###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()