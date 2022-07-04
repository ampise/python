import os, sys
os.system("clear")

def getFahrenheit():
    fahrenheit = (float(sys.argv[1]) * 1.8) + 32
    print(sys.argv[1], "ºC =", fahrenheit, "ºF")
    

def getCelsius():
    celsius = (float(sys.argv[2]) - 32) * (5/9)
    print(sys.argv[2], "ºF =", celsius, "ºC")

# MAIN PROGRAM

if len(sys.argv) >= 2:
    print(getFahrenheit(), getCelsius())
else:
    print("Incorrect usage. Correct usage: python 3 ", sys.argv[0], "C F")