def binary_search(lst, target):
    """
    Args:
        lst: sorted list
    Returns: 
        True/False
    """
    def helper(lst, target, lo, hi):
        if hi < lo or lo < 0 or hi >= len(lst) or \
                target < lst[lo] or target > lst[hi]:
            return False
        mi = lo + (hi - lo) // 2
        mid_elem = lst[mi]
        if target == mid_elem: return True
        elif target > mid_elem: return helper(lst, target, mi+1, hi)
        else: return helper(lst, target, lo, mi-1)
    return helper(lst, target, 0, len(lst) - 1)


for i in xrange(11):
    print i, binary_search([1,2,3,4,5,6,8,9], i)