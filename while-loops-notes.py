# We use loops to repeat some set of instructions
# While Loops are used to repeat until some condition is met, that is, we don't know up from how many repeats are needed

# Initialize loop variable
x = 0
# Condition to check
while (x < 10):
    # Indented code is what gets repeated
    print(x)
    # Last indented line is where we change the loop variable
    x = x + 3

# Doesn't get printed if not indented
print ("Code goes here when the loop ends.")

# Important: If we forget to include the last line, which changes our loop variable, we have an infinite loop. The loop will never end and our program will probably not function how we like.
# Condition (Inside th parentheses after the while command word) must be something that can evaluate to True or False

# When comparing in our while loop conditions, we use the same set of opertators as we use for if commands: <, >, <=, >=, ==, !=

#  Example 1
# Wrote a while loop the prints the numbers starting at 15, ending at 0 (inclusive), ant counts down by 3.

n = 15
while n >= 0:
    print(n)
    n = n - 3

# What happens if we move the last statement to be the first inside the loop?

n = 15
while n >= 0:
    n = n - 3
    print(n)

# Answer: All of the output is shifted. We will now start at 12 and end at -3, neither of which is correct for this problem

# Write a program that prints your name some number of times. Start counting at 1. After you print your name, decide if the current count is even or odd. If even, add 3 to your count. If odd, add 1 to your count. Stop when the count is greater than 100.

count = 1

while count <= 100:
    print("Ananya", count)
if count % 2 == 0:
    count = count + 3
else:
    count = count + 1

# Two special while loops uses are Diagnostic while loop and a Sentinel while loop.

# Diagnostic while loop is used to check for a bad user input
# Diagnostic loops check for failure

# Ask the user to input a positive number

number = int(input("Please enter a positive number: "))
# Checking for bad data
while number <= 0:
    print("Sorry, incorrect value.")
    number = int(input("Please enter a positive number: "))

# Write a Diagnostic Loop that asks the user to input a number that is less than 100.

number = int(input("Please enter a number that is less than 100: "))
while number >= 100:
    print("Sorry, incorrect value. Again, enter a number less than 100.")
    number = int(input("Please enter a number that is less than 100: "))

# Sentinel while loops allow the user to easily restart a program from the beginning

again = "Y"
while again == "Y":
    print("This is where your program does what it does!")
    # Note that your whole program goes within this while loop
    again = input("Would you like to run this program again? (Y/N): ")
print ("End of program. Thanks!")

# Write a while loop that adds all of the numbers between 1 and 1000 (inclusive)

add = 1
all = 0
while add <= 1000:
    all = all + add
    add = add + 1
print("Total: " + all)