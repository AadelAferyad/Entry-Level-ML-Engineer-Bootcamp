#!/usr/bin/python3

from tqdm import tqdm
from time import sleep 

def ft_progress(lst):
    for i in lst:
        yield i

listy = range(1000)

def main():
    for i in tqdm(ft_progress(listy)):
        sleep(0.25)

main()
