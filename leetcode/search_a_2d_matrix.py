from bisect import bisect_left

def binary_search(a, target, lo=0, hi=None):
    if hi is None: hi = len(a)
    rt = bisect_left(a, target, lo, hi)
    return rt if rt != hi and a[rt] == target else -1;

# print binary_search([1,2,3,4,5,6], 0)
# print binary_search([1,2,3,4,5,6], 1)
# print binary_search([1,2,3,4,5,6], 2)
# print binary_search([1,2,3,4,5,6], 3)
# print binary_search([1,2,3,4,5,6], 4)
# print binary_search([1,2,3,4,5,6], 5)
# print binary_search([1,2,3,4,5,6], 6)
# print binary_search([1,2,3,4,5,6], 7)


def search_matrix(matrix, target):
    def bisect_left_row():
        lo, hi = 0, len(matrix)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target > matrix[mid][0]: lo = mid + 1
            else: hi = mid
        return lo
    
    row_hint = bisect_left_row()
    if row_hint != len(matrix) and matrix[row_hint][0] == target:
        row_num = row_hint
    else:
        row_num = row_hint - 1
        
    row = matrix[row_num]
    col_num = bisect_left(row, target)
    if col_num == len(row) or row[col_num] != target:
        col_num = -1
    return row_num, col_num

m = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print search_matrix(m, 3)
print search_matrix(m, 16)
print search_matrix(m, 19)
print search_matrix(m, 25)
print search_matrix(m, 50)
print search_matrix(m, 58)