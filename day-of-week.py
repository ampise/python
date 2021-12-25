import os, math
os.system("clear")

DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
userDate = input("Enter a date [mm/dd/yy]: ")
dt = list(map(lambda x: int(x) ,userDate.split("/")))

# Divide year by 4
calc = math.floor(dt[2] / 4)
# Add day
calc = calc + dt[1]
# Add month's key value
# https://www.wikihow.com/Calculate-the-Day-of-the-Week
keys = [0,3,3,6,1,4,6,2,5,0,3,5]
calc = calc + keys[dt[0]-1]
# Subtract 1 for Jan or Feb of a leap year
if (dt[0] == 1 or dt[0] == 2) and dt[2] % 4 == 0:
    calc = calc - 1
    print("That was a leap year!")
# Add 2 digits of year
calc = calc + dt[2]
calc = int(calc % 7)

print("That day was ", DAYS[calc - 1])