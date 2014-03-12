def trap(A):
    def left_highest(array):
        rt = []
        max_so_far = -1
        for i in array:
            max_so_far = max(i, max_so_far)
            rt.append(max_so_far)
        return rt

    lh = left_highest(A)
    rh = list(reversed(left_highest(reversed(A))))
    rt = 0 

    for i in xrange(1, len(A) - 1):
        trap_h = min(lh[i - 1], rh[i + 1])
        if A[i] < trap_h:
            rt += (trap_h - A[i])
    return rt

print trap([0,1,0,2,1,0,1,3,2,1,2,1])