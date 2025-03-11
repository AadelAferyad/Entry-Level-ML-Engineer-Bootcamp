#!/usr/bin/python3

from sys import argv as av

def main():
    if (len(av) != 3):
        print("ERROR")
        return None
    if (not av[1].isalnum() and av[1].isdigit()):
        print("ERROR")
        return None
    if (not av[2].isdigit()):
        print("ERROR")
        return None

    n = int(av[2])
    l = av[1].split(' ')
    same_length = [i for i in l if len(i) > n]
    valid = []
    for x in same_length:
        a = 1
        for i in x:
            if i in "?.,!":
                a = 0;
                break ;
        if a:
            valid.append(x)
             
    print(valid)


main()
