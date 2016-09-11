#! /usr/bin/python
# https://github.com/jackchi/interview-prep

# Merge Sort
# Recursively divide arrays into 2 sorted arrays
# Merge two sorted arrays

# Big-O: n*ln(n)
# n time complexity to merge
# ln(n) time complexity to divide == height of the tree

def mergeSort(arr):
    """
    Base Case: 1 item array
    Recursive Case: divide at midpoint and call mergeSort on two arrays
    """
    # Base case
    if (len(arr) <= 1)
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """ Takes 2 sorted arrays and compares one element at a time
    to return one sorted array

    left = [1, 5, 6]
    right = [2, 3, 4]
    merge(left, right)
    [1, 2, 3, 4, 5, 6]

    """

    if not right:
        return left
    if not left:
        return right
    if left[0] < right[0]:
        return left[0] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])

l = [99,100]
r = [1,2,3,4,5,6]
print merge(l, r)