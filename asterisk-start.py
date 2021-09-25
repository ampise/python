import os
os.system("clear")

RANGE = 8
NUM_COLS = 3
for col in range(0, RANGE + 1, 2):
    if col == 0:
        col = "*"
    for row in range (NUM_COLS):
        print(col, end = " ")
    print()