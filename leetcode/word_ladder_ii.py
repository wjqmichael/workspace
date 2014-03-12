import collections
import string

class Solution:
    def build_prev(self, start, end, dict):
        '''
        Returns: dict of word to set of prev words
        '''
        rt = collections.defaultdict(set)
        current = [start]
        done = False
        while current and not done:
            nxt_level = []
            for word in current:
                tmp_word = list(word)
                for i in xrange(len(tmp_word)):
                    for ch in string.lowercase:
                        tmp_word[i] = ch
                        nu_word = ''.join(tmp_word)
                        if nu_word == end:
                            done = True
                            rt[nu_word].add(word)
                        if nu_word in dict:
                            rt[nu_word].add(word)
                            nxt_level.append(nu_word)
                    tmp_word[i] = word[i]
            for w in nxt_level:
                if w in dict:
                    dict.remove(w)
            current = nxt_level
        return rt

    def build_paths_helper(self, prev, tmp, rt):
        word = tmp[0]
        if not prev[word]:
            rt.append(tmp[:])
            return
        for w in prev[word]:
            tmp.insert(0, w)
            self.build_paths_helper(prev, tmp, rt)
            tmp.pop(0)

    def build_paths(self, prev, end):
        rt = []
        tmp = [end]
        self.build_paths_helper(prev, tmp, rt)
        return rt

    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        if start in dict:
            dict.remove(start)
        prev = self.build_prev(start, end, dict)
        print prev
        if not prev[end]:
            return []
        return self.build_paths(prev, end)

# print Solution().findLadders('hit', 'cog', set(["hot","dot","dog","lot","log"]))
print Solution().findLadders("red", "tax", set(["ted","tex","red","tax","tad","den","rex","pee"]))