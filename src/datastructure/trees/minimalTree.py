#! /usr/bin/python
# https://github.com/jackchi/interview-prep
# Copyright 2016 Jack Chi

# Given an array in sorted order, generate a BinaryTree with minimal height
# 4.2 in CtCT

from BinaryTree import *

# Matching # of nodes on left and right as much as possible
# 1. Insert mid element into tree
# 2. Set left tree = MinimalTree(left subarray)
# 3. Set right tree =  MinimalTree(right subarray)
def minimalTree(array):
	'''
	:param array: sorted array with increasing integer values
	:return: BinaryTree with minimal height
	'''
	if len(array) == 0:
		return None

	length = len(array)
	mid = length/2
	left = array[:mid]
	right = array[mid+1:]

	tree = BinaryTree(array[mid])
	tree.leftChild = minimalTree(left)
	tree.rightChild = minimalTree(right)
	return tree


heights = [6, 7, 8, 10, 14, 15, 17, 21, 22]

heightMHT = minimalTree(heights)

print BinaryTree.getHeight(heightMHT)








