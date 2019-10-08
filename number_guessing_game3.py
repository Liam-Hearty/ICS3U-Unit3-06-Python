#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: September 2019
# This program makes the user guess the random number.


import random


def main():
    random_number = (random.randint(0, 9))
    chosen_number = input("Enter your guess between 0-9: ")

    try:
        chosen_number = int(chosen_number)
        if int(chosen_number) == random_number:
            print("Correct!!")
        else:
            print("Wrong! the number was:{0} ".format(random_number))
    except ValueError:
        print("That was not a number between 0-9.")
    finally:
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
