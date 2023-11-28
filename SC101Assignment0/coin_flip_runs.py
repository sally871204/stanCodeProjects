"""
File: coin_flip_runs.py
Name: 許景涵
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


'''
# 我寫的
def main():
	"""
	Number of runs: enter a positive integer. This is the number of the consecutive results on either 'H' or 'T'.
	The program will randomly generate a string of coin flip results and will stop when reaching the number of runs.
	"""
	print("Let's flip a coin!")
	num_run = int(input('Number of runs: '))

	# Initial values
	consecutive_count = 0
	last_flip = None
	result = 'Result: '  # The string

	while True:
		flip = r.randint(0, 1)
		if flip == 0:
			result += 'H'
		else:
			result += 'T'

		if flip == last_flip:
			consecutive_count += 1
		else:
			consecutive_count = 0
		last_flip = flip

		if consecutive_count >= num_run:
			print(result)
			break
'''


# 解答範本
def main():
	"""
	This program will flip the coin until flip results
	reach the number of runs entered by the user.
	"""
	print("Let's flip a coin!")
	# Asking the user to enter the number of runs.
	num_run = int(input('Number of runs: '))
	# Setting initial conditions before looping the runs counting loop.
	result = ''      # Recording all the flip results. Starting with empty string.
	number = 0       # Counting the number of runs.
	if_run = False   # The status of whether the result is consecutive.
	# The loop won't stop unless the flip results reaches the runs set by the user.
	while num_run != number:
		coin = flip(n)                # The new flip result.
		result += coin               # Recording all the flip results.
		if len(result) > 1:          # Checking process of runs starts with 2nd flip.
			last = result[len(result) - 2]  # The last result before this new result.
			# Checking whether the new flip result equals the last one.
			if last == coin:         # True. The result is consecutive.
				# Checking whether this consecutive result is a new run.
				if not if_run:       # True. When if_run is False, this is a new run.
					if_run = True    # Turning if_run into True to start this run.
					number += 1      # The number of runs increases by 1.
			else:                    # False. The result is not consecutive.
				if_run = False       # if_run must be False if not consecutive.
	print(result)  # Printing out all the flip results when the loop ends.


def flip(n):
	# Initial values
	flip1 = r.randrange(1, 3)
	switch = False    # 把初始開關設成 False
	run = 0           # 連續次數
	ans = str(flip1)

	while True:
		if run == n:  # 連續次數 = user輸入次數
			break
		else:
			flip2 = r.randrange(1, 3)
			if flip1 == flip2:     # ex: HH
				if not switch:     # 把開關開啟
					run += 1
					switch = True  # 把開關關閉
			else:                  # ex: HHT
				switch = False     # 把開關開啟，進入上方 if not switch
			flip1 = flip2
			ans += str(flip1)
	return ans


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
