#!/usr/bin/python3

from tqdm import tqdm

def ft_progress(lst):
    for i in range(lst):
        yield i

listy = range(1000)

def main():
    for i in tqdm(ft_progress(listy)):
        sleep(0.01)

main()
