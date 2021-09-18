import os
os.system("clear")

likes = 0
name = input("Hi! Please input your name: ")

biking = input("Do you like to bike? (Y/N): ").upper()
if biking == "Y":
    likes += 1
reading = input("Do you like to read? (Y/N): ").upper()
if reading == "Y":
    likes += 1
math = input("Is math one of your favorite subjects? (Y/N): ").upper()
if math == "Y":
    likes += 1
organized = input("Do you consider yourself to be organized? (Y/N): ").upper()
if organized == "Y":
    likes += 1
languages = input("Do you like learning new languages? (Y/N): ").upper()
if languages == "Y":
    likes += 1

if likes >= 3:
    print(name, ", we have a lot in common! I think we would make great friends!")
else:
    print("Looks like we don't have much similarities, but it wouldn't hurt to be friends!")


# likableAttributes = ["biking", "swimming", "reading", "math", "learning languages", "be organized", "playing badminton"]
# for l in range(len(likableAttributes)):
#     ask = input("Do you like " + likableAttributes[l] + ". (Y/N) ").upper()
#     if ask == "Y":
#         likes += 1
# if likes >= round(len(likableAttributes) * 0.5):
#     print(name, ", we have a lot in common! I think we would make great friends!")
# else:
#     print("Looks like we don't have much similarities, but it wouldn't hurt to be friends!")
