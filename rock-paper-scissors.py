from genericpath import exists
import os, random, datetime, json
os.system("clear")

# Take input from user about their choice.
# Randomly generate choice and print.
# After each round, declare the winner by recalling the rules.
# At the end of the game, declare the final winner.

# Rock BEATS Scissors
# Paper BEATS Rock
# Scissors BEAT Paper

# def generateLogFile():
#     """
#     Format Codes	Description	Example
#     %d	Day of the month as a zero-padded decimal number	01, 02, 03, 04 …, 31
#     %a	Weekday as an abbreviated name	Sun, Mon, …, Sat
#     %A	Weekday as the full name	Sunday, Monday, …, Saturday
#     %m	Month as the zero-padded decimal number	01, 02, 03, 04, 05,…, 12
#     %b	Month as an abbreviated name	Jan, Feb, Mar,…, Dec
#     %B	Month as full name	January, February, …, December
#     %y	A year without century as the zero-padded decimal number	00, 01, 02, 03, …, 99
#     %Y	The year with century as the decimal number	0001, …, 2018, …, 9999
#     %H	Hour (24-hour clock) as the zero-padded decimal number	01, 02, 03, 04, 05 …, 23
#     %M	Minute as a zero-padded decimal number	01, 02, 03, 04, 05 …, 59
#     %S	Second as a zero-padded decimal number	01, 02, 03, 04, 05 …, 59
#     %f	Microsecond is the decimal number, zero-padded on the left	000000, 000001, …, 999999
#     %I	Hour (12-hour clock) as a zero-padded decimal number	01, 02, 03, 04, 05 …, 12
#     %p	Locale’s equivalent of either AM or PM	AM, PM
#     %j	Day of the year as a zero-padded decimal number	01, 02, 03, 04, 05 …, 366
#     """
#     today = datetime.datetime.now()
#     return today.strftime("Scores_%Y%m%d%H%M%S.txt")

INPUT_CHOICES = ['R','P','S']
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
lastRound = 0

# Check if this is a partial game. If directory exists, it is.
if os.path.isfile("rock-paper-scissors/savepoint.json"):
    savepoint = open("rock-paper-scissors/savepoint.json", "r")
    results = json.loads(savepoint.read())
    computerWins = results.get("computer")
    userWins = results.get("user")
    lastRound = results.get("round")
    savepoint.close()
    print("Previous incomplete game found. Resuming...")
else:
    if not os.makedirs("rock-paper-scissors/"):
        os.removedirs("rock-paper-scissors/")
        os.makedirs("rock-paper-scissors/")

for round in range(lastRound, ROUNDS):
    print("\nROUND: ", round + 1)
    computerChoice = random.choice(INPUT_CHOICES)
    userChoice = input("Enter [R]ock, [P]aper, or [S]cissor: ").upper()
    while not userChoice in INPUT_CHOICES:
        randomCorrections = [
            "Sorry, choice must be between R, S or P",
            "Oops, that was an incorrect entry. Must be between R, S or P",
            "Invalid value. Response must be between R, S or P",
            "Your input doesn't look within valid values. Response must be between R, S or P",
            "Your response was incorrect. Please enter a value between R, S or P"
        ]
        print("\n[!] ", random.choice(randomCorrections))
        userChoice = input("Enter [R]ock, [P]aper, or [S]cissor: ").upper()
        
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

    # Save results
    savepoint = open("rock-paper-scissors/savepoint.json", "w")
    savepoint.write(
        json.dumps({
            "computer": computerWins,
            "user": userWins,
            "round": round + 1
        })
    )
    savepoint.close()

if computerWins > userWins:
    print("\n\t ***************** \n\t     Computer Won! \n\t *****************")
elif computerWins < userWins:
    print("\n\t ***************** \n\t     User Won! \n\t *****************")
else:
    print("\n\t ***************** \n\t     Draw! \n\t *****************")

# Saved results cleanup
os.remove("rock-paper-scissors/savepoint.json")
os.removedirs("rock-paper-scissors/")