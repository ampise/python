import os
os.system("clear")

NUM_SCORES = 3
totalScore = 0
for n in range(NUM_SCORES):
    # Asking user to enter score for respective number of total courses
    score = input("Please enter score for course " + str(n + 1) + ": ")
    # Updates total score based on new score input
    totalScore = totalScore + int(score)

print("Average score of " + str(NUM_SCORES) + " is {:.2f}".format(totalScore / NUM_SCORES))
