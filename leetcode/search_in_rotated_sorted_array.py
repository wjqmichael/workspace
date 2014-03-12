def search(a, target):
    start, end = 0, len(a) - 1
    while start <= end:
        mid = start + (end - start) / 2
        if a[mid] == target:
            return mid
        if a[start] < a[mid]:
            if a[start] <= target < a[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if a[mid] < target <= a[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

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