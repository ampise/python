import os
os.system("clear")

# User input
num = int(input("Please enter a number to find the factorial: "))

# Initialize factorial
factorial = 1

# Check if number provided is negative, zero, or positive
if num < 0:
    print("Sorry, please enter a positive number.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of ", num, "is ", factorial)


