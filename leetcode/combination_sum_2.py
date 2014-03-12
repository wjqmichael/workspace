def combination_sum2(nums, target):
    def helper(index, left):
        # print comb, index, left
        for i in xrange(index, len(nums)):
            comb.append(nums[i])
            new_left = left - nums[i]
            if new_left == 0:
                rt.add(tuple(comb[:]))
                comb.pop()
                return
            elif new_left < 0:
                comb.pop()
                return
            else:
                helper(i + 1, new_left)
                comb.pop()

    nums.sort()
    rt = set()
    comb = []
    helper(0, target)
    return rt


nums = [10,1,2,7,6,1,5]
target = 8
print combination_sum2(nums, target)
