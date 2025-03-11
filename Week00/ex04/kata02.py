#!/usr/bin/python3

kata = (2019, 9, 25, 3, 30)


def main():
    a = 9
    print(f"{kata[1] if kata[1] > 9 else '0' + str(kata[1])}/{kata[2]}/{kata[0]} {kata[3] if kata[3] > 9 else '0' + str(kata[3])}:{kata[4] if kata[4] > 9 else '0' + str(kata[4])}")

main()
