import os, random
os.system("clear")

# Create Arrays (4)
special = ["$", "@", "_", "!"]
capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Password rules configuration
MAX_LENGTH = 30
MAX_CAPITAL = 5
MAX_SPECIAL = 5
MAX_NUMERIC = 5

# Initialize password requirements
generatedPassword = ""
passwdLength = 0
hasCapital = 0
hasSpecial = 0
hasNumeric = 0

# Pick a random character from randomly selected given lists 
def pickCharacter():
    characterArrays = {
        1: capital,
        2: special,
        3: lower,
        4: numbers
    }
    arr = characterArrays.get(random.randint(1, len(characterArrays)))
    return arr[random.randint(0, len(arr)-1)]

# Check if character exists in alphabets
def isACharacter(c, set):
    if set == "capital":
        alphabets = capital
    elif set == "lower":
        alphabets = lower
    elif set == "special":
        alphabets = special
    elif set == "numeric":
        alphabets = numbers
    elif set == "alphabets":
        alphabets = lower + capital
    for i in range(len(alphabets)):
        if c == alphabets[i]:
            return True
    return False

while passwdLength < MAX_LENGTH:
    tmp = pickCharacter()
    if len(generatedPassword) == 0:
        if isACharacter(tmp, "alphabets"):
            if isACharacter(tmp, "capital"):
                hasCapital = hasCapital + 1
            generatedPassword = generatedPassword + tmp
            passwdLength = passwdLength + 1
    else:
        if isACharacter(tmp, "special"):
            if hasSpecial >= MAX_SPECIAL:
                continue
            else:
                hasSpecial = hasSpecial + 1
        if isACharacter(tmp, "capital"):
            if hasCapital >= MAX_CAPITAL:
                continue
            else:
                hasCapital = hasCapital + 1
        if isACharacter(tmp, "numeric"):
            if hasNumeric >= MAX_NUMERIC:
                continue
            else:
                hasNumeric = hasNumeric + 1
        generatedPassword = generatedPassword + tmp
        passwdLength = passwdLength + 1

# Print generated password
print(generatedPassword)
