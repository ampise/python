import os, sys
os.system("clear")


text = str(sys.argv[1])

def getVowels():
    vowelsFound = []
    count = 0
    for vowels in text:
        if vowels in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            count += 1
            vowelsFound.append(vowels)
    print("A total of", count, "vowels were found.")
    print("They are: " + ", ".join(vowelsFound))
    # if count == 0:
        # print("Sorry, there were no vowels.")

# MAIN PROGRAM

if len(sys.argv) >= 2:
    print(getVowels())
else:
    print("Incorrect usage. Correct usage: python3" + sys.argv[0] + " NN")