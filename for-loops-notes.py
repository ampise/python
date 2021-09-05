# For loops are used for repeating a set of steps when we know the number of times
# While loops, on the other hand, are used when we don't know the number of times

# While Loop

x = 3
while x < 10:
    print(x)
    x = x + 2

# For Loop
# For the basic range statement, 3 values are used. They are the starting value, the ending value, and the count by value

for x in range (3, 10, 2):
    print(x)

# If we only have 2 values, the count value is assumed to be +1, and the remaning numbers are the start and stop values

print()
for x in range (3, 10):
    print(x)
print()

# If we only have 1 value in the range statement, it is the stop value
# The starting value is assumed to be 0. the step will continue to be assumed to be +1

for x in range (10):
    print(x)

# Find and print all of the positive numbers less than 200 and which are evenly divisible by 7

for n in range (7, 200, 7):
    print(n)

# Print all the numbers that are multiples of 5, starting at 250 and ending at 0 (inclusive)

for n in range (250, -1, -5):
    print(n)

# Be careful when counting backwards; You must specify the step value in this case
# The code below doesn't print anything since it is trying to count by +1

for y in range (250, -1):
    print(y)

# In addtion to a for loop that uses a range statement, we have a special type of for loop called a "For-Each" Loop that is usd for strings and lists

for letter in "VALUABLE":
    print(letter)

# Count the number of "e" in the name Tennessee

count = 0

for letter in "TENNESSEE":
    if(letter == "E"):
        count += 1
print(count)

myList = [3, 6, 9, 12, 15, 18]
total = 0
for num in myList:
    total += num
print(total)