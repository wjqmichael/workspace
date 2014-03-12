def multiply(num1, num2):            
    l1 = len(num1)
    l2 = len(num2)
    rt = [0] * (l1 + l2)

    for i1 in xrange(l1 - 1, -1, -1):
        carry = 0
        for i2 in xrange(l2 - 1, -1, -1):
            tmp = (ord(num1[i1]) - ord('0')) * (ord(num2[i2]) - ord('0')) + \
                rt[i1 + i2 + 1] + carry
            rt[i1 + i2 + 1] = tmp % 10
            carry = tmp / 10
        rt[i1] = carry

    rt_str = ''
    while rt and rt[0] == 0:
        rt.pop(0)
    for i in rt:
        rt_str += (chr(ord('0') + i))
    return rt_str if rt_str else '0'

assert(multiply('100', '100') == str(100 * 100))
assert(multiply('1324', '6543') == str(1324 * 6543))
assert(multiply('5132', '90') == str(5132 * 90))
assert(multiply('000', '13523') == '0')
assert(multiply('000', '00') == '0')
