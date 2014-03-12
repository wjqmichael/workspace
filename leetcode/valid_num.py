def is_number(s):
    def helper(s):
        if not len(s):
            return False, ''
        i = 0
        if s[0] == '-':
            i += 1
        if not s[i].isdigit():
            return False, ''
        i += 1
        while s[i].isdigit():
            i += 1
        if s[i]

    s = s.strip()
    if not len(s):
        return False

    if not s[0].isdigit():
        return False
    i = 1
    while i < len(s) and s[i].isdigit():
        i += 1
    if s[i] == '.':




assert(is_number('0'))
assert(is_number('  0.1  '))
assert(not is_number('abc'))
assert(not is_number('1 a'))
assert(is_number('2e10'))