import os
os.system("clear")

bits = [256, 128, 64, 32, 16, 8, 4, 2, 1]
userInput = int(input("Enter a number to convert into Binary format: "))

binary = []
for i in bits:
    if (userInput - i) >= 0:
        binary.append(1)
        userInput = userInput - i
    else:
        binary.append(0)

b = map(lambda x: str(x), binary)
print("Binary equivalent is "," ".join(b))