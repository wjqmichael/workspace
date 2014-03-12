def isMatch(s, p):
    '''
    * matches any sequence of chars,
    ? matches any single char
    '''
    def helper(s, si, p, pi):
        if pi == len(p):
            return si == len(s)
        
        pc = p[pi]
        if pc != '*':
            return si != len(s) and (
                (pc == '?' or s[si] == pc) and helper(s, si + 1, p, pi + 1))
        
        for i in xrange(si, len(s) + 1):
            if helper(s, i, p, pi + 1):
                return True
        return False
        
    return helper(s, 0, p, 0)


assert(not isMatch("aa","a"))
assert(isMatch("aa","aa"))
assert(not isMatch("aaa","aa"))
assert(isMatch("aa", "*"))
assert(isMatch("aa", "a*"))
assert(isMatch("ab", "?*"))
assert(not isMatch("aab", "c*a*b"))