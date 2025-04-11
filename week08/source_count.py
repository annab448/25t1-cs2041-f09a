#!/usr/bin/env python3
from glob import glob
# from collections import defaultdict
# collections.defaultdict => defaultdict

def main():
    total = 0
    for filename in glob(r'*.[ch]'):
        with open(filename) as f:
            subtotal = len(f.readlines())
            print(f"{subtotal: 6} {filename}")
            total += subtotal
    print(f"{total: 6} total")


if __name__ == "__main__":
    main()