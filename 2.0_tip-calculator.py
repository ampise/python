import os, sys
os.system("clear")

billTotal = float(sys.argv[1])
tipPercent = float(sys.argv[2]) / 100

def getTip():
    finalAmount = (1 + tipPercent) * billTotal
    print("Final Amount: \t${:0,.2f}".format(finalAmount))

# MAIN PROGRAM

if len(sys.argv) >= 2:
    print(getTip())
else:
    print("Incorrect usage. Correct usage: python 3 ", sys.argv[0], "$ %")


