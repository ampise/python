# Boolean Variable is any variable that has one of two possible values: True or False

loop = True
choice = False

# In general, most values are treated as "True" by the computer
# Things that are considered "False": , the empty string "", the key words False and None
# Any time we evaluate a condition, we are using boolearn values
# The condition is either evaluated as True or False

x = 13
if x < 15:
    # Computer converts x < 15 to a boolean result
    print("Yes.")

# Will this print?

if 37:
    print("???")
    # Yes, it will, 37 is considered true, as it doesn't meet any criteria for False

# Using boolean is conditional statements.
# Never compare a varable to True of False using ==

# This is wrong to do

# cond = True
# if cond == True:
    # print("This is wrong!")

# This is much better

# cond = True
# if cond:
    # print("Do it this way.")

# The problem with the above is that it only works if we want to know if something is True
# What if we want to know if it is False?
# The first logical operator is "not" and it helps us solve this problem

found = False
if(not found):
    print("Still looking...")

# In general, the not operator switches a boolean value to it's opposite state

test = True
if test:
    print("1")
if(not test):
    print("2")
if(not(not(not(test)))):
    print("3")

# The other logical operatos will allow us to build more complex conditions
# These operators are "and" and "or"

# And - Joins two or more conditions together. In order for the full condition to be considered True, all parts must be True
# Otherwise it is False

test = True
test2 = False

if test and test2:
    print("4")
if test and test:
    print("5")
if not test and test2:
    print("6")
if test and not test2:
    print("7")

# Or - Joins two more more contitions together. In order for the full condition to be true, at least one of the conditions must be true
# Only false if all parts are false

if test or test2:
    print("8")
if test or test:
    print("9")
if not test or test2:
    print("10")
if test or not test2:
    print("11")

# DeMorgan's Law
# Applies when we have a complex condition with a not in the front

x = 10
test = True
if(not(x < 13 and test)):
    print("???")

# When applying DeMorgan's Law:
# - All boolean values get a not added/dropped: test -> not test; not here -> here
# - Math equations flip the sige: <= becomes >, < becomes >=, != becomes ==
# - and becomes or, or becomes and

# We are going to make use of this for a diagnostic loop that has complex conditions. 
# Ask user for number less than 100 and greater than or equal to 0
# Success will be (num < 100 and num >= 0)
# We check for failure in a diagnostic: not(num < 100 and num >= 0)