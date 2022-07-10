import os, sys, math
os.system("clear")

def getMin(max, a):
    min = max
    for i in a:
        if i < min:
            min = i
    return min

def getMax(a):
    max = 0
    for i in a:
       if i > max:
           max = i
    return max

def getDeviation(a):
    # Calculate mean
    sum = 0
    mean = 0
    for i in a:
        sum = sum + i
    mean = sum / len(a)
    # Calculate deviation
    sum = 0
    for i in a:
        sum = sum + ((mean - i) ** 2)
    sd = math.sqrt(sum / len(a))
    return sd


# MAIN PROGRAM

if len(sys.argv) >= 2:
    list = []
    for i in range(1, len(sys.argv)):
        list.append(int(sys.argv[i]))

    mx = getMax(list)
    mn = getMin(mx, list)
    sd = getDeviation(list)
    print("Minimum of set: ", mn)
    print("Maximum of set: ", mx)
    print("Standard Deviation of set: ", sd)

else:
    print("Incorrect usage. Correct usage: python3", sys.argv[0], "NN")