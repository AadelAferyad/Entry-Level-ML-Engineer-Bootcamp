#!/usr/bin/python3


kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def main():
    for k, v in kata.items():
        print(f'{k} was created by {v}')

main()
