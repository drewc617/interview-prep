#!/usr/bin/python
# Copyright 2016 Jack Chi
#
# Using Recursion and Generators to find all combinations of a String
import sys

def combination(string):
    """ Generator to yield the current combination """
    yield ''
    for i, d in enumerate(string):
        for comb in combination(string[i+1:]):
            yield d + comb



def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: string'

    combinations = []
    for c in combination(args[0]):
        print c
        combinations.append(c)

    print combinations

if __name__ == '__main__':
    main()