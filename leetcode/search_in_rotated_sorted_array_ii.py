def search(A, key):
    lo, hi = 0, len(A) - 1
    while lo <= hi:
        mid = lo + (hi - lo) / 2
        if A[mid] == key: return mid
        if A[lo] < A[mid]:
            if A[lo] <= key < A[mid]: hi = mid - 1
            else: lo = mid + 1
        elif A[mid] < A[hi]:
            if A[mid] < key <= A[hi]: lo = mid + 1
            else: hi = mid - 1
        else: lo += 1
    return -1


A = [1, 3, 1, 1]
print(search(A, 0))
print(search(A, 1))
print(search(A, 2))
print(search(A, 3))
print(search(A, 4))

A = [1, 1, 3, 1, 1]
print(search(A, 0))
print(search(A, 1))
print(search(A, 2))
print(search(A, 3))
print(search(A, 4))

a = [4,5,6,7,0,1,2]
assert(search([], 1) == -1)
assert(search(a, 4) == 0)
assert(search(a, 5) == 1)
assert(search(a, 6) == 2)
assert(search(a, 7) == 3)
assert(search(a, 0) == 4)
assert(search(a, 1) == 5)
assert(search(a, 2) == 6)
assert(search(a, 8) == -1)
assert(search(a, -3) == -1)