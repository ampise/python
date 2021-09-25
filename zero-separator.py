import os, math
os.system("clear")

RANGE = 9
MIDPOINT = math.ceil(RANGE / 2)
REPEAT_FOR = 4

for row in range(REPEAT_FOR):
    for col in range(1, MIDPOINT):
        print(col, end = " ")
    print("0", end = " ")
    for col in range(MIDPOINT + 1, RANGE + 1):
        print(col, end = " ")
    print()