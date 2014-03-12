# from bisect import bisect_left, bisect_right

'''
python library has bisect_left & bisect_right
But here let's implement our own bisect
'''

def bisect_left(A, target):
    lo, hi = 0, len(A)
    while lo < hi:        
        mid = lo + (hi - lo) // 2
        if A[mid] >= target: hi = mid
        else: lo = mid + 1
    return lo

def bisect_right(A, target):
    lo, hi = 0, len(A)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if A[mid] > target: hi = mid
        else: lo = mid + 1
    return lo

def search_range(A, target):
    '''
    Args:
        A: sorted list
    '''
    lo = bisect_left(A, target)
    if lo > len(A) - 1 or not A[lo] == target: return [-1, -1]
    hi = bisect_right(A, target)
    return [lo, hi - 1]

# search_range = search_range_2
assert(search_range([], 10) == [-1, -1])
assert(search_range([10], 10) == [0, 0])
assert(search_range([10], 1) == [-1, -1])

A = [5, 7, 7, 8, 8, 10]
assert(search_range(A, 5) == [0, 0])
assert(search_range(A, 7) == [1, 2])
assert(search_range(A, 8) == [3, 4])
assert(search_range(A, 10) == [5, 5])
assert(search_range(A, 6) == [-1, -1])
assert(search_range(A, -5) == [-1, -1])
assert(search_range(A, 100) == [-1, -1])