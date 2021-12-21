import os, random
os.system("clear")

# Generate random number R
LOWER = 10
UPPER = 100
CHANCES = 5
R = random.randint(LOWER, UPPER)
# print(" >> R = ", R)

# Find how far from lower and upper limits
lowerRangeHalf = round((R - LOWER) / 2, 0)
# print(" >> L = ", lowerRangeHalf)

upperRangeHalf = round((UPPER - R) / 2, 0) + R
# print(" >> U = ", upperRangeHalf)

# Loop 5 times (chances)
matched = False
chances = 1
while not matched and chances <= CHANCES:
    guess = int(input("Take a guess: "))
    chances = chances + 1

    if guess > R:
        if guess > upperRangeHalf:
            print("Oops! You went too far.")
        else:
            print("You are close, but still a little higher.")
    elif guess < R:
        if guess < lowerRangeHalf:
            print("Oops! You went too low.")
        else:
            print("Almost, but you are still lower.")
    else:
        matched = True
        print("You got it!")

# Reveal result
if chances >= CHANCES:
    print("Sorry you could not guess. The number was", R)