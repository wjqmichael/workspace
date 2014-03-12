class Solution:
    # @return a boolean
    '''
    2-dim dp: C[i][j] will be true if C[0..i+j-1]
    is an interleaving of A[0..i-1] and B[0..j-1].

    And it turns out we only need one dim as we only need one final answer.

    dp[i][j] = true if (dp[i][j-1] is true and B[j] == C[i+j-1]) 
        OR (dp[i-1][j] is true and A[i] == C[i+j-1])
    '''
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        if len(s1) < len(s2): ss, ls = s1, s2
        else: ss, ls = s2, s1
        dp = [True]
        dp += [ss[0:i + 1] == s3[0:i + 1] for i in xrange(len(ss))]

        for i in xrange(1, len(ls) + 1):
            for j in xrange(len(dp)):
                if j == 0: dp[j] = dp[j] and ls[i - 1] == s3[i - 1]
                else: dp[j] = (dp[j] and ls[i - 1] == s3[i + j - 1]) or \
                    (dp[j - 1] and ss[j - 1] == s3[i + j - 1])

        return dp[-1]

s = Solution()
print s.isInterleave('', '', '')