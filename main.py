# Programmers:  Cooper Nazar
# Course:  CS151, Professor Yalew
# Due Date: November 7, 2024.
# Programming Assignment:  PA 03
# Problem Statement: Allow the user to request ASCII art of a circle, create their own set of lines, or request a random design
# Data In: Which ASCII art to display, length of the lines, number of lines, and character that makes the lines
# Data Out: ASCII art
# Credits:

import random

# Purpose: Print a circle
# Parameters: None
# Return: None
def circle():
    print("\nCIRCLE")
    print(" " * 5, "_" * 5, " " * 5)
    print(" " * 3, "/", " " * 5, "\ ")
    print(" " * 2, "|", " " * 7, "| ")
    print(" " * 3, "\ ", " " * 4, "/")
    print(" " * 5, "-" * 5, " " * 5)

# Purpose: Print a snowman's head
# Parameters: None
# Return: None
def snowman():
    print("\nSNOWMAN")
    print(" " * 4, "_" * 7)
    print(" " * 4, "|", " " * 3, "|")
    print(" " * 4, "|", " " * 3, "|")
    print(" " * 4, "|", " " * 3, "|")
    print("-" * 18)
    print(" " * 3, "/", "O", " ", "O", "\ ")
    print(" " * 2, "|", " " * 7, "| ")
    print(" " * 2, "|", "0", " " * 3, "0", "| ")
    print(" " * 3, "\ ", "0" * 3, "", "/")
    print(" " * 5, "-" * 5, " " * 5)

# Purpose: Print a cat face
# Parameters: None
# Return: None
def rabbit():
    print("\nRABBIT")
    print(" " * 4, "|\ ", " ", "/|")
    print(" " * 4, "|", "\ ", "/", "|")
    print(" " * 5, "-" * 5, " " * 5)
    print(" " * 3, "/", "O", " ", "O", "\ ")
    print(" " * 2, "|", " " * 7, "| ")
    print(" " * 2, "|", "--", "V", "--", "| ")
    print(" " * 3, "\ ", "/", "\ ", "/")
    print(" " * 5, "-" * 5, " " * 5)

# Purpose: Print a circle
# Parameters: None
# Return: None
def cellphone():
    print("\nCELLPHONE")
    print(" " * 4, "-" * 5)
    print(" " * 3, "|", "-O-", "|")
    print(" " * 3, "||", " ", "||")
    print(" " * 3, "||", " ", "||")
    print(" " * 3, "||", " ", "||")
    print(" " * 3, "|", "-=-", "|")
    print(" " * 4, "-" * 5)

# Purpose: Check if the input is a number
# Parameters: Number
# Return: Number
def number_check(number):
    while not number.isdigit():
        print("Invalid input. Please input a number.")
        number = input("Please input a number: ")
    number = int(number)
    return number

# Purpose: Prompt the user to input the length, number, and character used to make lines, and print those lines
# Parameters: None
# Return: None
def lines():
    line_num = input("\nHow many lines do you want to make? ")
    line_num = number_check(line_num)
    length = input ("\nHow long do you want to make the lines? ")
    length = number_check(length)
    character = input("\nWhat character do you want the lines to be made out of?")
    count = 0
    while count <= line_num:
        print(f'{character * length}')
        count += 1

# Purpose: Display a random ASCII art out of three options
# Parameters: None
# Return: None
def random_art():
    art_num = random.randint(1, 3)
    if art_num == 1:
        snowman()
    elif art_num == 2:
        rabbit()
    else:
        cellphone()

# Purpose: Display a menu where the user can choose to see a circle, random art, or make lines
# Parameters: None
# Return: None
def menu():
    print("\nASCII Art Menu.")
    print("_" * 20)
    print("\t1. Circle")
    print("\t2. Make Lines")
    print("\t3. Random Art")
    print("_" * 20)
    decision = input("Which ASCII art would you like to see? Please input your decision as a number. ")
    number_check(decision)
    while decision != "1" and decision != "2" and decision != "3":
        print("Invalid input. Please input a number from the given list.")
        decision = input("Which ASCII art would you like to see? Please input your decision as a number.")
    if decision == "1":
        circle()
    elif decision == "2":
        lines()
    else:
        random_art()

def main():
    print("\nThis program is meant to allow you to view ASCII art.")
    menu()
    print("\nThanks for using this program!")

main()