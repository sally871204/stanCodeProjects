"""
File: class_reviews.py
Name: 許景涵
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""


def main():
    course = input('Which class? ')
    if course == '-1':
        print('No class scores were entered')
    else:
        # Initial values to save the scores
        # sc001_max = None
        # sc001_min = None
        # 這些初始值的選擇是為了確保任何輸入的得分都能正確更新最高分和最低分，因為任何得分都會比無窮小大，比無窮大小。
        # 隨著後續的得分輸入，這些初始值將逐漸被實際的最高分和最低分所取代。
        sc001_max = -float('inf')  # 無窮小，表示尚未記錄任何最高分，因為任何得分都會大於無窮小，所以後續得分將取代它。
        sc001_min = float('inf')   # 無窮大，表示尚未記錄任何最低分，因為任何得分都會小於無窮大，所以後續得分將取代它。
        sc001_total = 0
        sc001_count = 0            # Count how many scores there are in order to calculate the average score

        # sc101_max = None
        # sc101_min = None
        sc101_max = -float('inf')
        sc101_min = float('inf')
        sc101_total = 0
        sc101_count = 0

        while course != '-1':
            score = input('Score: ')  # Ask the user to input the score

            try:
                score = int(score)    # Convert the score to an integer
            except ValueError:        # If the score is not an integer, print 'score: ' again
                print('Score: ')
                continue

            # Update the data of SC001 & SC101
            if course.upper() == 'SC001':
                # if sc001_max is None or score > sc001_max:
                if score > sc001_max:
                    sc001_max = score  # Update sc001_max when the input score is higher than the previous score
                # if sc001_min is None or score < sc001_min:
                if score < sc001_min:
                    sc001_min = score  # Update sc001_min when the input score is lower than the previous score
                sc001_total += score
                sc001_count += 1
            elif course.upper() == 'SC101':
                # if sc101_max is None or score > sc101_max:
                if score > sc101_max:
                    sc101_max = score  # Update sc101_max when the input score is higher than the previous score
                # if sc101_min is None or score < sc101_min:
                if score < sc101_min:
                    sc101_min = score  # Update sc101_min when the input score is lower than the previous score
                sc101_total += score
                sc101_count += 1

            # Ask the user to input the class name (either SC001 or SC101) again
            course = input('Which class? ')

        # Show the results of Max, Min and Avg for SC001 & SC101
        print('=============SC001=============')
        if sc001_count > 0:
            print('Max (001): ' + str(sc001_max))
            print('Min (001): ' + str(sc001_min))
            print('Avg (001): ' + str(sc001_total / sc001_count))
        else:
            print('No score for SC001')

        print('=============SC101=============')
        if sc101_count > 0:
            print('Max (101): ' + str(sc101_max))
            print('Min (101): ' + str(sc101_min))
            print('Avg (101): ' + str(sc101_total / sc101_count))
        else:
            print('No score for SC101')


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
