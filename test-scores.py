import os
os.system("clear")

NUM_STUDENTS = 5
max = 0
min = 100
sum = 0

studentScores = []

# Accept scores from teacher
for i in range(NUM_STUDENTS):
    score = int(input("Enter score for student " + str(i + 1) + ": "))
    studentScores.append(score)

# Calculate max, min, and average of all scores
for score in studentScores:
    sum = sum + score
    if score > max:
        max = score
    if score < min:
        min = score
average = sum / len(studentScores)
# Print all calculations
print("Maximum score: ", max)
print("Minimum score: ", min)
print("Average of all scores: ", average)
