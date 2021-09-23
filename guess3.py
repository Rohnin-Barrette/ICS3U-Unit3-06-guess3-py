#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This function asks the user to guess a number between 1 and 10 and tells the user if the input isn't valid

import random


def main():
    # This function asks the user to guess a number between 1 and 9

    # input

    guessed_string = input("Enter a number between 1 and 10: ")
    print("")

    # process & output
    random_number = random.randint(1, 10)

    try:
        guessed_number = int(guessed_string)
        if guessed_number == random_number:
            print("YAAAAY you guessed it right!!!")
        else:
            print(" :( You got it wrong. it was actually {0} .".format(random_number))
    except Exception:
        print("{0} is not an integer.".format(guessed_string))
    finally:
        print("Thanks for playing")
        print("\nDone.")


if __name__ == "__main__":
    main()
