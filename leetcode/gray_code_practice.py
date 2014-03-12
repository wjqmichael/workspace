class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0: return [0]
        rt = ['0', '1']
        while n > 1:
            rt = ['0' + i for i in rt] + ['1' + i for i in reversed(rt)]
            n -= 1
        return [int(i, 2) for i in rt]

s = Solution()
print s.grayCode(3)