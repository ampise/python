boxHeight = float(input("What is the height of the box?: "))
boxWidth = float(input("What is the width of the box?: "))
boxLength = float(input("What is the length of the box?: "))
widgetHeight = float(input("What is the height of the widget)?: "))
widgetWidth = float(input("What is the width of the widget?: "))
widgetLength = float(input("What is the length of the widget?: "))
boxVolume = boxHeight * boxLength * boxWidth
widgetVolume = widgetWidth * widgetHeight * widgetLength
widgetNumber = boxVolume / widgetVolume

print("The number of widgets that can fit into the box: " + str(widgetNumber))