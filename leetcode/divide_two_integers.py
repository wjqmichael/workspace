def divide(dividend, divisor):
    
    def sign(dividend, divisor):
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return False
        return True

    dvnd = abs(dividend)
    dvsr = abs(divisor)    
    ret = 0

    while dvnd >= dvsr:
        add_to_ret = 1
        tmp_dvsr = dvsr
        while dvnd >= tmp_dvsr:
            dvnd -= tmp_dvsr
            ret += add_to_ret
            tmp_dvsr <<= 1
            add_to_ret <<= 1

    return ret if sign(dividend, divisor) else -ret


assert(divide(8, 1) == 8)
assert(divide(7, 2) == 3)
assert(divide(5, 5) == 1)
assert(divide(1, 1) == 1)
assert(divide(0, 3) == 0)