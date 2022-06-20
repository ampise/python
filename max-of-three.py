import os, sys
from webbrowser import get
os.system("clear")

def getMax(arr):
    max = 0
    for i in range(1, len(arr)):
        print(">>", arr[i])
        if int(arr[i]) > max:
            max = int(arr[i])
    return max

#-- main--
if len(sys.argv) >= 2:
    print(getMax(sys.argv))
else:
    print("Incorrect usage. Correct usage: python3" + sys.argv[0] + "NN")
