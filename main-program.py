import os
os.system("clear")

def main():
    print("Hello World!")
    # x = 10 / 0
    try:
        answer = int(input("What should I divide 10 by? "))
        print(10 / answer)
    except ZeroDivisionError as e:
        print("Division by zero! really?")
    except ValueError as e:
        print("Invalid input received")
        print(e)
    finally:
        print("End of the program")


if __name__ == "__main__":
    main()

