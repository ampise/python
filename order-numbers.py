import os, sys
os.system("clear")

# Order numbers provided by user from greatest to least.

def getMax(a):
    max = 0
    for i in a:
        if i > max:
            max = i
        return max

def getMin(max, a):
    min = max
    for i in a:
        if i < min:
            min = i
        return min



# MAIN PROGRAM
