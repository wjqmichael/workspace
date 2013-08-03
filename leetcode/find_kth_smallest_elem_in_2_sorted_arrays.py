'''
Given two sorted arrays A, B of size m and n respectively. 
Find the k-th smallest element in the union of A and B. 
You can assume that there are no duplicate elements.
'''

import sys

def findKth(a, b, k):
	"""
	a: list 1
	b: list 1
	k: targe (kth element)
	"""

	len1 = len(a)
	len2 = len(b)
	i = (k - 1) * len1 / (len1 + len2)
	j = k - 1 - i
	min_int = -sys.maxint - 1

	a_i_1 = min_int if i == 0 else a[i - 1]
	b_j_1 = min_int if j == 0 else b[j - 1]
	a_i = sys.maxint if i == len1 else a[i]
	b_j = sys.maxint if j == len2 else b[j]

	if (b_j_1 < a_i < b_j):
		return a_i
	if (a_i_1 < b_j < a_i):
		return b_j

	if (a_i < b_j):
		del a[0:i+1]
		del b[j+1:]
		return findKth(a, b, j)
	else:
		del b[0:j+1]
		del a[i+1:]
		return findKth(a, b, i)

print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 1)
print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 2)
print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 3)
print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 4)
print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 5)
print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 6)
print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 7)
print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 8)
print findKth([1, 3, 5, 7, 8, 9], [2, 4, 6], 9)
