#!/usr/bin/python3

from sys import argv

def main():
    length = len(argv) - 1
    if (length == 0):
        print("No enough arguments please enter some arguments : python3 exec.py 'test'")
        return ;
    while (length >= 1):
        string = argv[length][::-1]
        for c in string:
            print(c.lower() if c.isupper() else c.upper(), end="")
        length = length - 1

main()
