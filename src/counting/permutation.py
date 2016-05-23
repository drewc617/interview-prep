#!/usr/bin/python
# https://github.com/jackchi/util
# Copyright 2014 Jack Chi

# Python Recursion: String Permutation
# Recursion is made up of two cases
# - base case where it doesn't recurse
# - recursive case where it calls itself with different parameter

# Remove the first item
# Find permutation of the remaining items
# Reinsert the item removed in every possible location
import sys

def getPermutations(word):
    if len(word) < 2:
        return word
    else:
        results = []
        for i, letter in enumerate(word):
            for j in getPermutations(word[:i]+word[i+1:]): # remaining word
                results.append(letter+j)
    return results

def permute(s):
    if not s:
        yield ''
    for i, c in enumerate(s):
        for perm in permute(s[:i] + s[i+1:]):
            yield c + perm

def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: string [string2]'
        sys.exit(1)
    for word in args:
        print '%s has these permutations:\n' % word + str(getPermutations(word)).strip('[]')

if __name__ == '__main__':
    main()

