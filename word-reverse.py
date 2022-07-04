import os, sys
os.system("clear")

def getReversed():
    text = sys.argv[1] [::-1]
    print(text)

if len(sys.argv) >= 2:
    print(getReversed())
else:
    print("Incorrect usage. Correct usage: python 3", sys.argv[0], "NN")