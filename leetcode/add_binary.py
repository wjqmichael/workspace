def add_binary(a, b):
    num = max(len(a), len(b))
    rt = ''
    carry = 0
    for i in xrange(num):
        if i > len(a) - 1:
            da = 0
        else:
            da = int(a[-1-i])
        if i > len(b) - 1:
            db = 0
        else:
            db = int(b[-1-i])

        s = da + db + carry
        carry = 1 if s >= 2 else 0
        nxt = s % 2
        rt = str(nxt) + rt
    if carry:
        rt = '1' + rt
    return rt

print add_binary('1', '11')
print add_binary('1111', '1111')