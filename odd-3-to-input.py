# Have the user input a number greater than 10 and less than 20, and verify that the number is within that range. 
# Then create a loop that will run and print all the odd numbers staring at 3 and ending on the number that was inputted (inclusive).

import os
os.system("clear")

# accept input
# check if in range
# loop from 3 to input
# print if odd
# if not in range exit
number = int(input("Enter a number: "))
if number > 10 and number < 20:
    for n in range(3, number + 1):
        # if number is not even, it is odd
        if n % 2 != 0:
            print(n)
else:
    print("Sorry, invalid. Try again.")

