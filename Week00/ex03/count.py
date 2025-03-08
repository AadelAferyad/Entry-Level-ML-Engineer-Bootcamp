#!/usr/bin/python3

def check_data(data):
    l = ['?', '.', ',', '!']
    printable = 0
    lowercase = 0
    uppercase = 0
    punctuation = 0
    spaces = 0
    for i in data:
        if i.isprintable():
            printable += 1
        if (i.isalpha()):
            if (i.islower()):
                lowercase += 1
            else:
                uppercase += 1
        if i.isspace():
            spaces += 1
        if i in l:
            punctuation += 1;
    print(f"The text contains {printable} printable character(s):")
    print(f"- {uppercase} upper letter(s)")
    print(f"- {lowercase} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {spaces} space(s)")

def text_analyzer(data):
    """ This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text. """
    if not data:
        print("What is the text to analyze?")
        data = input()
    if isinstance(data, int) or data.isdigit():
        print("argument is not a string")
        return None
    check_data(data)

def main():
    length = len(av)
    if (length - 1 > 1):
        print("Error more than one argument is provided")
        return None
    data = None
    if length - 1 == 1:
        data = av[1]
    text_analyzer(data);

if __name__ == '__main__':
    from sys import argv as av
    main()
