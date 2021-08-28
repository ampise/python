# Print the number 4 and "Hello, there!"
print(4)
print("Hello, there!")

# We can also make the system print values that we have saved in variables
x = 42
print(x)
print("x")

# If you put quotes around a value you will print whatever you put inside the quotes
# No quotes means a variable name and you will the value of the variable, not its name

# We can print multiple values in the same print command
# Simply seperate them with commas

print("The value of the variable is", x)

# The comma will generate one space when printed

# To print a single blank line, put nothing in the parentheses

print("Hello!")
print()
print("World!")

# This is called an "Empty Print"
# We use escape sequences to print certain characters and some special values
# All of these sequences start with a backslash (\)

# For quotes, you can do this

print("\"Hello.\" ")

# Prints "Hello." including the quotes around it

# We can print tabs using \t

print("The\tCat")

# We can print extra line breaks using \n

print("This will\nappear on\n three lines.")

# We have to use an escape sequence to print a backslash, \\
print("Neat\\Trick")

# There are a nuber of formatting options we can include to make the code look more inviting

print("Text(:^10.2f): {} More Text".format("value1, value2"))

# Formatting is always going to start with a colon (:)
# Then comes justification < (Left Justify) > (Right Justify) ^(Center Justify)

# Next is the number of spaces I want the data to fit into
# Finally, number of decimal places .2f will only show 2 decimal places

import math
print("coll{} col2".format(math.pi))
print("coll {:.2f} col2".format(math.pi))
print("coll {:15.2f} col2".format(math.pi))
print("coll {:^15.2f} col2".format(math.pi))

# To make columns equal, we can use \t, but it is not recommended
print("coll\tcol2\tcol3")
print("Hello\tFantastic\tScrumptious\tDessert Pie")

# Using formatted print statements can solve the problem of misaligned data when we have either really short or really long data

print("{:15}{:15}{:15}".format("coll","col2","col3"))
print("{:15}{:15}{:15}".format("Meow","A","Scrumptious"))

# Input Statements
# Variable = input("User Prompt")

number = input("Please enter a number: ")
print(number)

# When you use an input command, Python always reads the value as a string
# In order to read in numbers, you need to cast the data

number = int(input("Please enter a number: "))
print(number + 3)

# To get a floating point number we use "float" instead of "int"

number = float(input("Please enter a number: "))
print(number)

# When in doubt, use "float" to read in numbers
# "Float" is more flexible

