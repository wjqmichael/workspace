class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [1] * (n + 1)
        for i in xrange(2, n + 1):
            tmp = 0
            for j in xrange(i):
                tmp += dp[j] * dp[i - 1 - j]
            dp[i] = tmp
        return dp[-1]

s = Solution()
print s.numTrees(3)