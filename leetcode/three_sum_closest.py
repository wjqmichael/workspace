import sys

def three_sum_closest(num, target):
    closest = sys.maxint
    result = 0
    len_num = len(num)
    num.sort()
    for i in xrange(len_num - 2):
        j = i + 1
        k = len_num - 1
        while (j < k):
            sum = num[i] + num[j] + num[k]
            if abs(sum - target) < closest:
                result = sum
                closest = abs(sum - target)
            if sum - target > 0:
                k -= 1
            elif sum - target < 0:
                j += 1
            else:
                return sum
    return sum

assert(three_sum_closest([-1, 2, 1, -4], 1) == 2)
