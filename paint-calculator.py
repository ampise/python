wallLength = input("Enter wall length: ")
wallWidth = input("Enter wall width: ")
wallHeight = input("Enter wall height: ")
windows = input("How many windows are in the room?: ")
doors = input("How many doors are in the room?: ")
WINDOW_AREA = 15
DOOR_AREA = 20
PAINT_AREA = 350.0

totalSurfaceArea = 2 * ((wallLength * wallHeight) + (wallHeight * wallWidth))
unPaintableArea = (windows * WINDOW_AREA) + (doors * DOOR_AREA)
paintableArea = totalSurfaceArea - unPaintableArea
totalPaintGallons = paintableArea / PAINT_AREA

print("Total paint area: {:0,.2f}".format(paintableArea))
print("Total gallons of paint needed: {:0,.2f}".format(totalPaintGallons))
