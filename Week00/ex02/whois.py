#!/usr/bin/python3

from sys import argv

def main():
    length = len(argv)
    if (length - 1 == 0):
        print("[Usage]: Please enter an argument (INTEGER)")
        return ;
    if length - 1  > 1:
        print("more than one argument is provided")
        return None
    if not argv[1].isdigit():
        print("argument is not integer")
        return None
    n = int(argv[1])
    if (n == 0):
        print("I'm Zero.");
    elif (n % 2):
        print("I'm Odd.");
    else:
        print("I'm Even.");

main()
