#!/usr/bin/env python3
import sys

def main():
    # error check cmd line args
    if (len(sys.argv) != 4):
        print(f"Usage: {sys.argv[0]} <n_rows> <n_cols> <col_width>")
        sys.exit(1)
    try:
        n_rows = int(sys.argv[1])
        n_cols = int(sys.argv[2])
        col_width = int(sys.argv[3])
    except ValueError as e:
        print(f"{sys.argv[0]}: expected integers")
        sys.exit(1)
    for y in range(1, n_rows + 1):
        for x in range(1, n_cols + 1):
            product = x*y
            print(f"{product: <{col_width}}", end='')
        print('')

if __name__ == "__main__":
    main()