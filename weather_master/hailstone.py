"""
File: hailstone.py
Name: 許景涵
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program executes the Hailstone sequence after entering a number.
    """
    print('This program computes Hailstone sequences.')
    n = int(input('Enter a number: '))
    count = 0
    while n > 1:
        if n % 2 == 1:       # n is odd
            result = 3*n + 1
            print(str(n) + ' is odd, so I make 3n+1: ' + str(result))
        else:                # n is even
            result = n//2
            print(str(n) + ' is even, so I take half: ' + str(result))
        n = result
        count += 1
    print('It took ' + str(count) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
