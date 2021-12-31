import os
os.system("clear")

for i in range(5, 0, -1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print()

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()

line = -1
for i in range(5, 0, -1):
    line = line + 1
    for l in range(line):
            print(" ", end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

