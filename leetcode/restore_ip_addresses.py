class Solution:
    def is_valid(self, s):
        # if s == '': return False
        i = int(s)
        if i != 0 and s[0] == '0': return False
        if i == 0 and len(s) > 1: return False
        return (0 <= i <= 255)

    # @param s, a string
    # @return a list of strings
    '''
    The tricky part is to determine the ending param of xrange for i, j, and k.
    We are used to writing a <= i <= b, while xrange range doesn't include
    the ending argument. 
    So make sure to add 1 to b for the arg of xrange
    '''
    def restoreIpAddresses(self, s):
        rt = []
        if len(s) < 4: return rt

        for i in xrange(min(3, len(s) - 3)): # i is the ending position (included) of the first part
            if not self.is_valid(s[0:i + 1]): continue
            for j in xrange(i + 1, min(i + 4, len(s) - 2)):
                if not self.is_valid(s[i + 1: j + 1]): continue
                for k in xrange(j + 1, min(j + 4, len(s) - 1)):
                    if not self.is_valid(s[j + 1: k + 1]) or \
                            not self.is_valid(s[k + 1:]):
                        continue
                    rt.append('.'.join([s[0:i + 1], s[i + 1: j + 1], 
                        s[j + 1: k + 1], s[k + 1:]]))
        return rt

s = Solution()
print s.restoreIpAddresses('25525511135')
print s.restoreIpAddresses('0000')