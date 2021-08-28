yearUser = int(input("Enter your year of birth: "))

if yearUser >= 1900 and yearUser <= 2021:
    age = 2021 - yearUser
    if age == 0:
        print("Hello, little baby!!")
    else:
        print("You are " + str(age) + " years old.")
else:
    print("Cannot calculate.")
