class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        if not S or not T: 
            return 0
        dp = [0] * len(T)
        if S[-1] == T[-1]:
            dp[-1] = 1
        for m in reversed(xrange(len(S) - 1)):
            for n in xrange(len(T) - 1):
                if T[n] == S[m]:
                    dp[n] += dp[n + 1]
            if S[m] == T[-1]:
                dp[-1] += 1
        return dp[0]
