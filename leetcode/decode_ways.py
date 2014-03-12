# The following solution works, but has O(2^n), too slow
# class Solution:
#     # @param s, a string
#     # @return an integer
#     def numDecodings(self, s):
#         def helper(ind, rt):
#             if ind > s_len: return
#             if ind == s_len: 
#                 rt[0] += 1
#                 return
#             if s[ind] == '0': return

#             helper(ind + 1, rt)
#             if ind + 1 <= s_len - 1 and 10 <= int(s[ind:ind+2]) <= 26:
#                 helper(ind + 2, rt)

#         s_len = len(s)
#         rt = [0]            
#         helper(0, rt)
#         return rt[0]

# This solution has O(n) and constant space. Pretty cool
class Solution:
    def numDecodings(self, s):
        if len(s) == 0: return 0
        if len(s) == 1: return 0 if s == '0' else 1

        last_two = [1, 0]
        for i in xrange(len(s) - 1, -1, -1):
            rt = 0
            # s[i] can be decoded
            if s[i] != '0': rt += last_two[0]
            # s[i: i + 2] can be decoded
            if i + 1 <= len(s) - 1 and 10 <= int(s[i: i + 2]) <= 26: 
                rt += last_two[1]
            # update last_two
            last_two.pop()
            last_two.insert(0, rt)
            if last_two[0] == 0 and last_two[1] == [0]: return 0
        return last_two[0]

