import os
os.system("clear")

rows = 7
for num in range(0, rows):
    for asterisk in range(0, num + 1):
        print("*", end = " ")
    print()