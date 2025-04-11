#!/usr/bin/env python3
import sys

def main():
    filename1, filename2 = sys.argv[1:3]
    print(f"comparing {filename1} and {filename2}")

    f1 = open(filename1)
    words1 = set()
    for line in f1:
        word = line.strip()
        words1.add(word)

    f1.close()

    words2 = set()
    with open(filename2) as f2:
        for line in f2:
            words2.add(line.strip())
    
    for word in sorted(words1 - words2):
        print(word)
if __name__ == "__main__":
    main()