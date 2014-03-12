def combinationSum(candidates, target):
    def helper(index, sum):
        if sum == 0:
            ret.append(lst[:])
            lst.pop()
            return
        for i in xrange(index, len(candidates)):
            nxt_sum = sum - candidates[i]
            if nxt_sum < 0:
                break
            lst.append(candidates[i])
            helper(i, nxt_sum)
        if lst: lst.pop()

    lst, ret = [], []
    candidates.sort()
    helper(0, target)
    return ret

assert combinationSum([2,3,6,7], 7) == [[2, 2, 3], [7]]