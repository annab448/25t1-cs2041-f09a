#!/usr/bin/env python3
import re, sys, subprocess
def main():
    url = sys.argv[1]
    proc  = subprocess.run(f'wget -q -O- {url}', shell=True, text=True, capture_output=True)
    webpage = proc.stdout

    # find anything that is made up of digits, spaces and hyphens
    ph_nums = set()
    for match in re.findall(r"[\d -]+", webpage):
        num = re.sub(r'\D', '', match)
        if len(num) >= 8 and len(num) <= 15:
            ph_nums.add(num)

    for num in ph_nums:
        print(num)
if __name__ == "__main__":
    main()