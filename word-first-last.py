from __future__ import print_function
import os, math
os.system("clear")

word = "Sunita"
wordMidpoint = int(len(word)/2)

last = len(word)
for f in range(0, wordMidpoint, 1):
    print(word[f], end=" ")
    last = last - 1
    for r in range(last, last - 1, -1):
        print(word[r], end=" ") 
if len(word) % 2:
    print(word[wordMidpoint])