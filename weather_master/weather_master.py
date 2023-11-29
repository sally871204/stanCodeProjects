"""
File: weather_master.py
Name: 許景涵
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program computes the highest, lowest, average temperatures
	and the number of cold days(<16 degree) among the weather data.
	"""
	print('StanCode "Weather Master 4.0"!')
	t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	if t == EXIT:
		print('No Temperatures were entered.')
	else:
		t_max = t_min = t
		# 第一個數設為最大值、最小值
		t_sum = t
		# 一開始的總和 = 第一個溫度 t
		t_count = 1
		cold_days = 0
		if t < 16:
			cold_days += 1
		while True:
			t = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if t == EXIT:
				break
			else:
				if t > t_max:
					t_max = t
					# 若後面的數 > 前面的數，後面的數變最大值
				if t < t_min:
					t_min = t
					# 若後面的數 < 前面的數，後面的數變最小值
			t_sum += t
			t_count += 1
			if t < 16:
				cold_days += 1
		print('Highest temperature = ' + str(t_max))
		print('Lowest temperature = ' + str(t_min))
		print('Average = ' + str(t_sum/t_count))
		print(str(cold_days) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
