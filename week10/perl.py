import sys

def chomp(string):
    if string[-1] == '\n':
        string = string[:-1]
    return string

def qw(string):
    return string.split(" ")

def die(err_msg):
    print(err_msg)
    sys.exit(1)