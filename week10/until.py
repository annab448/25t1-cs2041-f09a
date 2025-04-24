#!/usr/bin/env python3
import sys, re
import perl
from perl import chomp

# line number
#./until.py 9

# regex match
#./until.py /.3/
#./until.py X.3X

def main():
    if len(sys.argv) != 2:
        perl.die(f"Usage: {sys.argv[0]} <line_num or regex>")
    try:
        address = int(sys.argv[1])
    except ValueError:
        address = re.compile(sys.argv[1][1:-1])

    for line_no, line in enumerate(sys.stdin, 1):
        line = chomp(line)
        print(line)
        
        # check if address is line_num, regex object
        if isinstance(address, int):
            # address => integer
            if line_no == address:
                break
        else:
            # address => regex
            if address.search(line):
                break

if __name__ == "__main__":
    main()