import os, random
os.system("clear")

# Generate random number
num = random.randint(0,50)
counter = 0
guess = -1

# Tell user if number is larger or smaller
while num != guess:
    guess = int(input("Please guess a number between 0 to 50: "))
    if guess > num:
        print("Guess was larger than number.")
    elif guess < num:
        print("Guess was small.")
    counter += 1
print("Congrats! You got it after", counter, "tries.")
