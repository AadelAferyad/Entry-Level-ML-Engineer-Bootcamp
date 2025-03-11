#!/usr/bin/python

kata = "The right format"

def main():
    length = len(kata)
    
    for i in range(42 - length):
        print('-', end='')
    print(kata, end='')


main()
