'''
http://discuss.leetcode.com/questions/228/powx-n
O(lgn) time: half is not calucated more than once!
The formula is shown below:
x^n:
1.0, if n = 0
x^(n/2) * x^(n/2), if n is even
x^floor(n/2) * x^floor(n/2) * x, if n > 0 and is odd
x^ceil(n/2) * x^ceil(n/2) * x^(-1), if n < 0 and is odd

Please note that if we use the floor formula for n < 0 (though the formula 
    itself is correct), as floor(-1/2) = -1, we will get an infinite recursion.
'''
import math

def my_pow(x, n):
    if n == 0: 
        return 1.0
    hn = n/2 if n > 0 else math.ceil(n/2.0)
    half = my_pow(x, hn)
    if n % 2 == 0:
        return half * half
    elif n > 0:
        return half * half * x
    else:
        return half * half / x


assert(my_pow(2,0) == pow(2,0))
assert(my_pow(5,3) == pow(5,3))
assert(my_pow(2,0) == pow(2,0))
assert(my_pow(2,0) == pow(2,0))
assert(my_pow(2,0) == pow(2,0))
assert(my_pow(3,-2) == pow(3,-2))
