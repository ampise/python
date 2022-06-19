import os, random, math
os.system("clear")

# Computer generates random prime number between 1-100
# User guesses prime numbers in unlimited tries
# Computer tells if hot, cold, less, or more based on guess
# Hot Range: +/- 3 numbers | Cold Range:

primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# def getNextPrimeDivisor(n):
#     for i in range(2, n):
#         if isPrime(i):
#             if n % i == 0:
#                 return i
#     return n

# Generate random number R
def generateRandomNumber(): 
    LOWER = 1
    UPPER = 100
    CHANCES = 5
    R = random.choice(primeNumbers)
    print(" >> R = ", R)
    hotMore = primeNumbers[R] + 3

# Find how far from lower and upper limits
# lowerRangeHalf = round((R - LOWER) / 2, 0)
# print(" >> L = ", lowerRangeHalf)

# upperRangeHalf = round((UPPER - R) / 2, 0) + R
# print(" >> U = ", upperRangeHalf)

# Loop amount of chances
matched = False
chances = 1

while not matched and chances <= CHANCES:
    guess = int(input("Enter a prime number between 1 and 100: "))
    chances = chances + 1
    


# Check if input is prime
def isPrime(n):
    isPrime = True
    for i in range(2, n - 1):
        if n % i == 0:
            isPrime = False
            print("Input invalid. Please enter a prime number.")
            break
    return isPrime

# Reveal result
if chances >= CHANCES:
    print("Sorry, you guessed incorrectly. The number was", R)

# --- main execution ---
...