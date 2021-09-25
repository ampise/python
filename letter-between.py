import os
os.system("clear")

RANGE = 3
REPEAT_FOR = 3

for row in range(REPEAT_FOR):
    for col in range(1, RANGE + 1):
        print("A " + str(col), end = " ")
    print()