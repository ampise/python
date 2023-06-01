import os, random
os.system("clear")

def setupWarehouse(r, c, b):
    # Create an empty warehouse
    rows = []
    for y in range(r):
        cols = []
        for x in range(c):
            cols.append(0)
        rows.append(cols)
    # Place boxes randomly
    boxes = b
    while boxes > 0:
        x = int(random.uniform(1, c - 1))
        y = int(random.uniform(1, r - 1))
        if rows[x][y] <= 0:
            rows[x][y] = rows[x][y] + 1
            boxes = boxes - r
    return rows

def displayWarehouse():
    for x in range(len(warehouse)):
        print(warehouse[x])

def findBoxesInWarehouse():
    coords = []
    # 
    return coords

def findDistanceFromOrigin(x, y):
    distance = 0
    # 
    return distance

def removeBox(x, y):
    # 
    print("Box at " + str(x) + ", " + str(y) + " is removed")
    displayWarehouse()

# main

warehouse = setupWarehouse(10, 10, 5)
displayWarehouse()


