import os, sys
os.system("clear")

def getNumeral(n):
    numbers = [1000, 500, 100, 10, 5, 1]
    roman = {1: "I", 5: "V", 10: "X", 100: "C", 500: "D", 1000: "M"}
    numerals = []
    while n > 0:
        for i in numbers:
            if (n - i) >= 0:
                # print(">>", int(sys.argv[1]))
                # print(">>", i)
                n = n - i
                numerals.append(roman.get(i))
                break
    return "".join(numerals)
        

# MAIN PROGRAM
if len(sys.argv) >= 2:
    print(getNumeral(int(sys.argv[1])))
else:
    print("Incorrect usage. Correct usage: python3" + sys.argv[0] + " NN")
