#! /usr/bin/python
# https://github.com/jackchi/interview-prep

# Insertion Sort
# Iteratively find the 1st lowest, 2nd lowest and puts them into place

# Big-O n*n - case where all elements needs to be looked at

def indexOfMinimum(array, startIndex):
    minIndex = startIndex
    minValue = array[startIndex]

    for i in xrange(minIndex+1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
            minIndex = i
            
    return minIndex

def insertionsort(array):
    for i,a in enumerate(array):
        minIndex = indexOfMinimum(array, i)
        array[i], array[minIndex] = array[minIndex], array[i]

    return array

l =  [33, 788, 1, -14, 78, 11, 32, 11, 78, -1, -14]
print indexOfMinimum(l, 0)
print insertionsort(l)





