import os
import math
os.system("clear")

# Calculate area of a Square


def squareArea():
    side = int(input("What is the side length? "))
    print("Area of this square is " + str(side * side))


# Calculate perimeter of a Square
def squarePerimeter():
    side = int(input("What is the side length? "))
    print("Perimeter of this square is " + str(4 * side))


# Calculate area of a Triangle
def triangleArea():
    base = int(input("What is the base length? "))
    height = int(input("What is the height? "))
    print("Area of this triangle is " + str(0.5 * base * height))


# Calculate area of a Circle
def circleArea():
    radius = int(input("What is the radius length? "))
    print("Area of this circle is " + str(math.pi * radius ** 2))


# Calculate circumference of a Circle
def circleCircumference():
    radius = int(input("What is the radius length? "))
    print("Circumference of this circle is " + str(2 * math.pi * radius))


# Wrapper function
def calculateArea(shape):
    shapeCalculator = {
        "1": squareArea,
        "2": squarePerimeter,
        "3": triangleArea,
        "4": circleArea,
        "5": circleCircumference,
    }
    func = shapeCalculator.get(shape)
    func()
    print("\n")


# Main entry
print("What would you like to do?")
print("1. Area of a square")
print("2. Perimeter of a square")
print("3. Area of a triangle")
print("4. Area of a circle")
print("5. Circumference of a circle")
shape = input("(e.g. enter 1 to calculate area of a square) > ")
calculateArea(shape)
