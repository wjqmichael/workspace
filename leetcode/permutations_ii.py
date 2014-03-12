'''
One solution is to use the same algorithm as permutations.py, but use a set
to keep the distinct values only.

Here we are trying another algorithm:
Converting the problem to many sub-problems. In short:

(1) Swap the 1st element with all the elements, including itself.
(2) Then the 1st element is fixed, go to the next element.
(3) Until the last element is fixed. Output.

http://yucoding.blogspot.com/2013/04/leetcode-question-69-permutations.html
'''

def permuteUnique(iterable):
    def helper(iterable, start, result):
        if start >= len(iterable) - 1:
            return
        helper(iterable, start + 1, result)
        for i in xrange(start + 1, len(iterable)):
            if iterable[i] != iterable[start]:
                tmp = iterable[:]
                tmp[i], tmp[start] = tmp[start], tmp[i]
                result.append(tmp)
                helper(tmp, start + 1, result)

    result = [tuple(iterable)]
    helper(iterable, 0, result)
    return result

print permuteUnique([1,2])
print permuteUnique([1,1,2])
