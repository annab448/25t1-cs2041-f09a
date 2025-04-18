#!/usr/bin/env python3
import sys, subprocess, re
import argparse
import requests
from bs4 import BeautifulSoup
from collections import Counter

def main():
	# create an argument parser
	parser = argparse.ArgumentParser()

	# setting up our arguments
	# -f: print in frequency order
	parser.add_argument("-f", "--frequency", action="store_true", help="print tags by frequency")
	parser.add_argument("-l", "--linenumbers", action="store_true")

	parser.add_argument("url", help="url to fetch")

	# parse arguments
	args = parser.parse_args()

	# print args summary
	if (args.frequency):
		print("frequency!!")
	if (args.linenumbers):
		print("linenumbers!!")

	print(f"url={args.url}")

	return
	response = requests.get(args.url)
	webpage = response.text.lower()

	soup = BeautifulSoup(webpage, 'html5lib')

	tags = [tag.name for tag in soup.find_all()]
	tag_count = Counter()

	for tag in tags:
		tag_count[tag] += 1
	
	if args.frequency:
		for tag, freq in reversed(tag_count.most_common()):
			print(f"{tag} {freq}")

	else:
		# print normally
		for tag in sorted(tag_count):
			print(f"{tag} {tag_count[tag]}")


if __name__ == "__main__":
	main()
