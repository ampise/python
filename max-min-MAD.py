import os, sys
os.system("clear")

def getMin(max):
    min = max
    for i in range(1, len(sys.argv)):
        if int(sys.argv) < min:
            min = int(sys.argv[i])
    return min

def getMax():
    max = 0
    for i in range(1, len(sys.argv)):
        if int(sys.argv) > max:
            max = int(sys.argv[i])
    return max

def getDeviation():


list = []


# MAIN PROGRAM

if len(sys.argv) >= 2:
    print("Minimum of set: ", getMin(sys.argv))
    print("Maximum of set: ", getMax(sys.argv))
    print("Standard Deviation of set: ", getDeviation(sys.argv))

else:
    print("Incorrect usage. Correct usage: python3", sys.argv[0], "NN")