#!/usr/bin/env python3
import sys, collections

def print_dict(d):
    for key, val in d.items():
        print(f"[{key}] => {val}")

def main():
    fave_colours = {}
    colour_count = collections.Counter()
    colour_by_name = collections.defaultdict(list)
    while (line := sys.stdin.readline()):
        name, colour = line.split()
        colour = colour.lower()
        fave_colours[name] = colour
        colour_count[colour] += 1
        colour_by_name[colour].append(name)

    print_dict(fave_colours)
    print_dict(colour_count)
    print_dict(colour_by_name)

if __name__ == "__main__":
    main()