"""
File: quadratic_solver.py
Name: 許景涵
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


import math


def main():
	"""
	This program computes the roots of equation: ax^2 + bx + c = 0
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	if a == 0:
		print('a cannot be equal to 0')
		a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	dis = b*b - 4*a*c
	# dis 為判別式
	if dis > 0:
		x1 = (-b + math.sqrt(dis)) / 2*a
		x2 = (-b - math.sqrt(dis)) / 2*a
		print('Two roots: ' + str(x1) + ', ' + str(x2))
	elif dis == 0:
		x = -b / 2*a
		print('One root: ' + str(x))
	else:
		print('No real roots')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
