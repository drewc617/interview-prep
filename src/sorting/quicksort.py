#! /usr/bin/python
# https://github.com/jackchi/interview-prep

# Quick Sort Algorithm
# Complexity time of n2 but avg time nln(n)
# Avg case is nln(n)
# Worst case is n*n
# Since we could get very unlucky with the partitions
import pprint

# Sort a list of ints

def quicksort(arr):
    """
    Pick a Pivot
    Recursively put everything less than pivot to the left / greater to the right
    lesser and everything greater
    """
    if not arr:
        return []
    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot]) # a subarray of everything lesser than pivot
    greater = quicksort([x for x in arr[1:] if x >= pivot]) # a subarray of everything greater than pivot
    return lesser + [pivot] + greater

while True:
    b = True
    while b:
        try:
            s = raw_input("Enter Some Numbers Separated by spaces:")
            numbers = map(int, s.split())
            b = False
            break
        except:
            print ("Wrong Input!")

        sn= quicksort(numbers)
        pprint.pprint(sn)

        quit = str(raw_input("Continue(y/n)?"))
        if quit =='y' :
            print ("ok!")
        elif quit == 'n' :
            break
