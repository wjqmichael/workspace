def isScramble(s1, s2):
    leng = len(s1)
    dp = [[[False] * leng for i in xrange(leng)] for i in xrange(leng)]

    print dp

isScramble('123', '456')