#!/usr/bin/env python

import click
import csv
import random
import sys

@click.command()
@click.option('--swap/--noswap', default=False)
@click.argument('path', type=click.Path())
def quiz(path, swap):
        
    with open(path, 'r') as file:
        words = list(csv.reader(file))

    if any(len(word) != 2 for word in words):
        print('Your csv has invalid columns for some row')
        return

    if swap:
        words = list(list(reversed(word)) for word in words)

    while words:

        random.shuffle(words)

        for word in words:

            question = word[0]
            answer = word[1]

            print()
            print('   ' + question + ' = ', end='')
            response = input()
            print()

            if response == answer:
                words.remove(word)
                print('-- Good. --')
                print('{} words left. --'.format(len(words)))

            else:
                print('-- Wrong. --')
                print('The answer is \'{}\''.format(answer))

if __name__ == '__main__':
    quiz()
