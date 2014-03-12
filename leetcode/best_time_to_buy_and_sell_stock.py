import sys

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        rt = 0
        min_so_far = sys.maxint
        for p in prices:
            if p - min_so_far > rt:
                rt = p - min_so_far
            if p < min_so_far:
                min_so_far = p
        return rt

s = Solution()
print s.maxProfit([1,2,33,4,5])