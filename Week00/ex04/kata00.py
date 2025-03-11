#!/usr/bin/python3

kata = (19, 42, 21)

def main():
    length = kata.__len__()
    print(f'The {length} numbers are:', ', '.join([str(i) for i in kata]))
main()
