def min_distance(word1, word2):
    if len(word1) > len(word2):
        sw, lw = word2, word1
    else:
        sw, lw = word1, word2

    dp = range(len(sw) + 1)
    for i in xrange(1, len(lw) + 1):
        old = dp[:]
        dp[0] = i
        for j in xrange(1, len(dp)):
            dp[j] = min(dp[j - 1] + 1, old[j] + 1, old[j - 1] + 
                (1 if lw[i - 1] != sw[j - 1] else 0))

    return dp[-1]

print min_distance('hellow', 'world')
print min_distance('1234', '')
print min_distance('', '')
print min_distance('aaaa', 'aaaa')