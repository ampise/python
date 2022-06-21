import os, sys
os.system("clear")

numbers = [1000, 500, 100, 10, 5, 1]
roman = {1: "I", 5: "V", 10: "X", 100: "C", 500: "D", 1000: "M"}
numerals = []

def getNumeral():
    while int(sys.argv[1]) >= 0:
        for i in numbers:
            if (int(sys.argv[1]) - i) >= 0:
                print(">>", int(sys.argv[1]))
                print(">>", i)
                sys.argv[1] = int(sys.argv[1]) - i
                numerals.append(roman.get(i))
                break
        print("".join(numerals))

# MAIN PROGRAM

if len(sys.argv) >= 2:
    print(getNumeral())
else:
    print("Incorrect usage. Correct usage: python3" + sys.argv[0] + " NN")
