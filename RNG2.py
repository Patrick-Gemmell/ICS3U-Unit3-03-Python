#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: September 12 2019
# This program does a guessing game

import random


def main():
    # this function guess and compares number
    while True:
        # input
        guessed_number = int(input("Guess an integer from 0-9 "))

        # process and output
        print("")
        if guessed_number == random.randint(0, 9+1):
            print("Correct!")
            break
        else:
            print("Sorry that's wrong, guess again?")


if __name__ == "__main__":
    main()
