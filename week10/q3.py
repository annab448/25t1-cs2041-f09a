#!/usr/bin/env python3
import sys

def main():

    vowels = "aeiou"
    trans = str.maketrans(vowels + vowels.upper(), vowels.upper() + vowels)

    for line in sys.stdin:
        print(line.translate(trans), end="")

if __name__ == "__main__":
    main()