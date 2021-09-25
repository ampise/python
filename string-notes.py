string1 = "Scout Finch"
string2 = "Harry Potter"

# Concatenation can be used to join multiple strings into one larger string

print(string1 + string2)

# We cannot subtract strings as it will give error and not work
# We can mutiply strings, but cannot divide strings

print(string1 * 3)

# Important String Commands

# len() returns the length of the string
# Note: Counts everything between quotes including punctuation and spaces

print(len(string2))
print(len("!%^&**()@::||\/"))

# Case Conversion

# To convert to all uppercase, we use upper()
# To convert to lowercase, we use lower()

upperCase = string1.upper()
print(upperCase)

print(string2.lower())

# Finding and Replacing Characters in a String (Case Sensitive)

# Find command finds position of first matching letter or sequence

location = string1.find("c")
print(location)

# Note: When talking about position or location we start counting at 0
# Note: This means that the last position of a string is in the length -1

# We can also use Find to locate a whole string

location = string2.find("Pot")
print(location)

# What happens if Find doesn't find a match?

print(string1.find("z"))

# A result of -1 means the search value was not found

# Replace Command takes two inputs: What to replace and what to replace it with
# Also Case Sensitive

newString1 = string1.replace("Fi", "Be")
print(newString1)

# Replace will replace every thing that matches

print(string2.replace("r", "b"))

# Comparing Strings

# Sometimes we would like to be able to compare two strings
# Checking for = or ≠ is the same as checking numbers

word1 = "Pineapple"
word2 = "Banana"
word3 = "banana"

if word1 == word2:
    print("That's weird.")
if word1 != word2:
    print("Makes sense.")

# Comparisons of strings are Case Sensitive

if word2 == word3:
    print("???")

# We can also compare strings to see if one is greater than or less than another

if word1 > word2:
    print(word1, "is greater.")

# Order of strings is determined by placement alphabetically
# Letters that come first alphabetically are less than those that come later

if word2 > word3:
    print(word2, "is greater.")
if word2 < word3:
    print(word3, "is greater.")

# Lowercases are considered greater than uppercase letter due to their positioning on the ASCII Character Table

if "cat" > "cab":
    print("Yep.")
if "cat" < "cab":
    print("Nope.")

# Indexing is a way to access a single letter. We can do this for bother strings and lists, although far more common with lists

letter = string1[0]
print(letter)

# This takes the first letter of string1
# To help remember what this does, it is recommended reading the [] as "at postion"
# string1 [4] says "string1 at position 4"

# How would I print just the last letter of string2? Assume we can't see string2 to count it out.

print(string2[len(string2 - 1)])

# Positions start at 0, and the last position is length - 1
# The value inside the [] must be an integer