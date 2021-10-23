import os
os.system("clear")
import math

nums = input("Enter a list of numbers arranged in ascending order: ")
list = []
for n in nums.split():
    list.append(int(n))

# Average
sum = 0
for i in range(len(list)):
    sum += list[i]
average = sum / len(list)
print("Average: ", average)

# Items in List
print("Items: ", len(list))

# Median
print("Median: ", len(list) / 2)
# Need to fix median accuracy, for even and odd lists

# First Divisible by 5
for d in list:
    if d % 5 == 0:
        print("The first number divisible by 5: ", d)
        break

# Perfect Squares
for p in list:
  if math.sqrt(p) == p:
    print("First Perfect Square: ", p)
    break