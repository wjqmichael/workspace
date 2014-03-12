def count_and_say(n):
    
    def get_next(s):
        rt = ''
        ct = 1
        for i in xrange(1, len(s)):
            if s[i] == s[i - 1]:
                ct += 1
            else:
                rt += (str(ct) + s[i - 1])
                ct = 1
        rt += (str(ct) + s[-1]) 
        return rt

    rt = '1'
    for i in xrange(1, n + 1):
        rt = get_next(rt)
    return rt

print count_and_say(1)
print count_and_say(2)
print count_and_say(3)
print count_and_say(4)
print count_and_say(100)