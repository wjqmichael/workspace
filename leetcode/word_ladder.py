class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    '''
    There are two ways to find all the neighbors of word w: 
    1) scanning all words in the dict
    2) go through all the characters of w and change one character each time, 
        check if there exists a word in the dict.
    The second method wins when the dict is large:
    the time complexity of method 1) is O(n), n is len(dict)
    while that of method 2) is O(len(word) * Constant), where is constant is 26,
    as we change the character from a-z. Also note that dict is a set, so the
    existence check takes constant time.
    '''
    def next_level(self, word, dict):
        rt = []
        tmp = list(word)
        for i in xrange(len(tmp)):
            for c in string.lowercase:
                tmp[i] = c
                tmp_str = ''.join(tmp)
                if tmp_str in dict:
                    dict.remove(tmp_str)
                    if tmp_str != word:
                        rt.append(tmp_str)
            tmp[i] = word[i]
        return rt

    def ladderLength(self, start, end, dict):
        if start == end: return 0
        current = [start]
        rt = 1
        while current:
            nxt = []
            for w in current:
                if w == end:
                    return rt
                nxt += self.next_level(w, dict)
            current = nxt
            rt += 1
        return 0