#!/usr/bin/python3

from sys import argv

def main():
    length = len(argv)
    if (length - 1 == 1):
        return ;
    try:
        assert length - 1 != 1, "more than one argument is provided"
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
        return None
    try:
        assert isinstance(argv[1], int), "argument is not integer"
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
    n = int(argv[1])
    if (n == 0):
        print("I'm Zero.");
    elif (n % 2):
        print("I'm Odd.");
    else:
        print("I'm Even.");


main()
