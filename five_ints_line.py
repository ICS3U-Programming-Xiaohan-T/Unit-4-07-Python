#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: Apr 30, 2025
# This program prints the integers from 1000 to 2000, 5 per line


def main():
    # This function prints the integers from 1000 to 2000, 5 per line
    for number in range(1000, 2001):
        # Print the number followed by a space
        print(number, end=" ")

        # Check if the number is divisible by 5 and add a new line
        if number % 5 == 0:
            # Print a new line
            print()

    print("Thanks for using this program!")


if __name__ == "__main__":
    main()
