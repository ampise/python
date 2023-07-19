import os
os.system("clear")

# list = eval(input("Please give a list of numbers: "))
list = input("Please give a list of numbers: ").split()

for i in list:
    if int(i) % 2 == 0:
        print("Even(s):", i)

# not done yet, make for loop for odds, append into respective array