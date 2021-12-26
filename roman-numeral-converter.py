import os
os.system("clear")

# Roman Numerals:
# Ⅰ = 1
# V = 5
# X = 10
# C = 100
# D = 500
# M = 1,000

numbers = [1000, 500, 100, 10, 5, 1]
roman = {1: "I", 5: "V", 10: "X", 100: "C", 500: "D", 1000: "M"}

numerals = []

userInput = int(input("Enter a number to convert to Roman Numerals: "))

while userInput > 0:
    for i in numbers:
        if (userInput - i) >= 0:
            userInput = userInput - i
            numerals.append(roman.get(i))
            break
print("".join(numerals))