# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Inputs:
# ---------
# - Distance between 2 objects
# - Speed of object at point A
# - Speed of object at point B
#
# Output:
# -----------
# - At what distance from its starting point will object at point A pass object starting from point B?
#
#       (A) -> - - ?? (distance) - - - (X) - - - - - - - - - - - - - <- - (B)
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

distance_A_B_miles = float(
    input("What is the distance between the two starting points?: "))
speed_A_mph = float(input("What is the speed of the first vehicle?: "))
speed_B_mph = float(input("What is the speed of the second vehicle?: "))

# distance_A_X = ??

x = (speed_A_mph * distance_A_B_miles) / (speed_A_mph + speed_B_mph)
print("The distance at which the two vehicles will crash: " + str(x))
