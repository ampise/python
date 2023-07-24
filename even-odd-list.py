import os
os.system("clear")

# list = eval(input("Please give a list of numbers: "))
list = input("Please give a list of numbers: ").split()
evens = []
odds = []

for e in list:
    if int(e) % 2 == 0:
        evens.append(e)
print("Even(s):", evens)

for o in list:
    if int(o) % 2 != 0:
        odds.append(o)
print("Odd(s):", odds)