import os
os.system("clear")

num = int(input("Please provide a number greater than 1: "))

# Check if given number is prime
prime = True
for factor in range(2, num):
    if num % factor == 0:
        prime = False
        break

if prime:
    print("It is prime")
else:
    print("It is NOT prime")
