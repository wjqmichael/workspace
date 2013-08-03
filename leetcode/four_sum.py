def four_sum(num, target):
    result = set()
    leng = len(num)
    num.sort()

    for i in xrange(leng - 3):
        for j in xrange(i + 1, leng - 2):
            m = j + 1
            n = leng - 1
            while m < n:
                sum = num[i] + num[j] + num[m] + num[n]
                if sum == target:
                    result.add((num[i], num[j], num[m], num[n]))
                if sum >= target:
                    n -= 1
                else:
                    m += 1

    return result

assert(four_sum([1,0,-1,0,-2,2], 0) == set([(-1, 0, 0, 1), (-2, -1, 1, 2), 
    (-2,  0, 0, 2)]))