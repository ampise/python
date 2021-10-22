# List is a group of values that are related in some way
# In Python, they are contained in [] and seperated by commas

muppets = ["Kermit", "Gonzo", "Fozzie", "Miss Piggy", "Beaker"]
sesame = ["Big Bird", "Zoe", "Cookie Monster", "Oscar"]

# A number of operations that worked for strings also apply to lists

# Concatenation

print(muppets + sesame)

# Creating repeated strings using operator works

print(muppets * 3)

# Using the length command to find the length of a list

length = len(sesame)
print(length)

# Indexing works the exact same as well. We use indexing to get access to on specific item from list
# Like before, the first item in the list is at postition zero

print(muppets[0])

# Print the last Sesame Street character

print(sesame[len(sesame) - 1])

# The Find and Replace commands don't work for lists

# Special commands that work only for lists and not for strings

# To add items to a list we use an Append Command

muppets.append("Statler")
print(muppets)

# We can add items to the middle of the list using insert

muppets.insert(3, "Waldorf")
print(muppets)

# Note: When using insert, nothing is lost/overwritten. We just move all the other values out one spot to make room

# To take items out of the list, we use remove. This removes only the first match found starting at the front of list

muppets.remove("Beaker")
print(muppets)

# There are two ways we will use for loops to process the data in a list

# Method 1:

myList = [2, 4, 6, 8, 10, 12, 14]
for i in myList:
    print(i)

# In this loop, the loop variable (i) is the value of the items in this list
# Useful when we want to visit every location in a list
# Useful when not changing the list in any way
# Easier of the loops to use

# Method 2:

myList = [2, 4, 6, 8, 10, 12, 14]
for i in range(0, len(myList)):
    print(myList[i])

# In this loop, the loop variable (i) is the position of the items in the list
# We have to use indexing to get the actual values from the list
# Useful when visiting only some positions in the list
# Useful when need to change data in a list
# Useful when more interested in the position rather than the values

# Example: Add 3 to every value in the list

myList = [2, 4, 6, 8, 10, 12, 14]
for i in range(0, len(myList)):
    myList[i] = myList[i] + 3
print(myList)

# Example: Find the sum of all the numbers in myList

sum = 0
for i in range(0, len(myList)):
    sum += myList[i]
print(sum)

# Print all the values in the odd numbered positions

for i in range(1, len(myList), 2):
    print(myList[i])

# Several common algorithims for lists
# Finding value in list, finding how many of a value occurs in list, finding the largest/smallest item in a list, finding the sum/average
