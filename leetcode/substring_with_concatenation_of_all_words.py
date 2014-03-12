def find_sub_string(s, L):
    ret = []
    if not L: 
        return ret

    word_len = len(L[0])
    total_len = word_len * len(L)
    
    for start in xrange(len(s) - total_len + 1):
        lst_cp = L[:]
        idx = start
        while lst_cp:
            word = s[idx : idx + word_len]
            try:
                lst_cp.index(word)
            except:
                break
            lst_cp.remove(word)
            idx += word_len
        if not lst_cp:
            ret.append(start)

    return ret

assert(find_sub_string("barfoothefoobarman", ["foo", "bar"]) == [0, 9])
assert(find_sub_string("", ["foo", "bar"]) == [])
assert(find_sub_string("barfoothefoobarman", []) == [])
assert(find_sub_string("aaaaaaa", ['a', 'a']) == [0,1,2,3,4,5])