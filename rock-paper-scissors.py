import os, random
os.system("clear")

# Take input from user about their choice.
# Randomly generate choice and print.
# After each round, declare the winner by recalling the rules.
# At the end of the game, declare the final winner.

# Rock BEATS Scissors
# Paper BEATS Rock
# Scissors BEAT Paper

ROUNDS = 5
RULES = {
    "R" : {
        "R": "-",
        "P": "P",
        "S": "R"
    },
    "P" : {
        "R": "P",
        "P": "-",
        "S": "S"
    },
    "S" : {
        "R": "R",
        "P": "S",
        "S": "-"
    }
}

# Initialize
computerWins = 0
userWins = 0

for i in range(ROUNDS):
    computerChoice = random.choice(['R','P','S'])
    userChoice = input("Enter [R]ock, [P]aper, or [S]cissor: ")

    #     Alternate approach 
    #  ------------------------
    # if computerChoice == "R":
    #     if userChoice == "R":
    #         print("Draw!")
    #     elif userChoice == "S":
    #         computerWins = computerWins + 1
    #         print("Computer won!")
    #     else:
    #         userWins = userWins + 1
    #         print("User won!")
    # elif computerChoice == "P":
    #     if userChoice == "R":
    #         computerWins = computerWins + 1
    #         print("Computer won!")
    #     elif userChoice == "S":
    #         userWins = userWins + 1
    #         print("User won!")
    #     else:
    #         print("Draw!")
    # elif computerChoice == "S":
    #     if userChoice == "R":
    #         userWins = userWins + 1
    #         print("User won!")
    #     elif userChoice == "S":
    #         print("Draw!")
    #     else:
    #         computerWins = computerWins + 1
    #         print("Computer won!")

    print("Computer's choice was ", computerChoice)
    win = RULES.get(computerChoice).get(userChoice)
    if win == "-":
        print("Draw!\n")
    else:
        if computerChoice == win:
            computerWins = computerWins + 1
            print("Computer won with choice ", computerChoice, "\n")
        else:
            userWins = userWins + 1
            print("User won with choice ", userChoice, "\n")

if computerWins > userWins:
    print("\n\t ***************** \n\t     Computer Won! \n\t *****************")
elif computerWins < userWins:
    print("\n\t ***************** \n\t     User Won! \n\t *****************")
else:
    print("\n\t ***************** \n\t     Draw! \n\t *****************")