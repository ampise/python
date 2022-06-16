# Objective: List the prime factors of any given number.
import sys, os, math
os.system("clear")

def isPrime(n):
    isPrime = True
    for i in range(2, n - 1):
        if n % i == 0:
            isPrime = False
            break
    return isPrime

def getNextPrimeDivisor(n):
    for i in range(2, n):
        if isPrime(i):
            if n % i == 0:
                return i
    return n

def isDivisible(n, f):
    if n % f == 0:
        return True
    return False

def getNextPrimeFactor(n):
    quotient = n
    divisor = getNextPrimeDivisor(n)
    quotient = int(n / divisor)
    return divisor, quotient

def verifyFactors(fs):
    product = 1
    for i in factors:
        product = product * i
    return product

# --- main execution ---
if len(sys.argv) > 1:
    n = int(sys.argv[1])
    factors = [1]
    while n > 1:
        d, n = getNextPrimeFactor(n)
        factors.append(d)

    print("Prime factors of " + sys.argv[1] + " are:")
    print(", ".join(map(str, factors)))
else:
    print("\nIncorrect usage. \nCorrect Usage: python3 prime-factors.py NN\n")
