def max_sub_array(A):
    'Kadane algorithm, run in O(n)'
    max_so_far = 0
    max_ending_here = 0
    for i in xrange(len(A)):
        max_ending_here = max(max_ending_here + A[i], 0)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_sub_array_2(A):
    'Divide and conquer, run in O(nlogn)'
    def get_max(left, right):
        if left == right:
            return A[left] if A[left] > 0 else 0
        mid = left + (right - left) / 2
        rt = max(get_max(left, mid), get_max(mid + 1, right), max_cross(left, mid, right))
        return rt

    def max_cross(left, mid, right):
        left_max = 0
        accumulate = 0
        for i in xrange(mid, left - 1, -1):
            accumulate += A[i]
            left_max = max(left_max, accumulate)

        right_max = 0
        accumulate = 0
        for i in xrange(mid + 1, right + 1):
            accumulate += A[i]
            right_max = max(right_max, accumulate)

        return left_max + right_max

    return get_max(0, len(A) - 1)

assert(max_sub_array_2([-2, -5, 6, -2,-3,1,5,-6]) == 7)
assert(max_sub_array_2([-2,1,-3,4,-1,2,1,-5,4]) == 6)