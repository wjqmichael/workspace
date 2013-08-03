import sys

def charToDigit(c):
	return ord(c) - ord('0')

def atoi(str):
	sign = True
	if (str[0] == '-'):
		sign = False
		str = str[1:]
	result = 0
	overflow = False
	for i in xrange(len(str)):
		digit = charToDigit(str[i])
		if result >= (sys.maxint - digit)/10:
			result = long(result)
		result = result * 10 + digit
	if not sign:
		result = -result
	return result

assert(atoi("-12345678901") == -12345678901)
assert(atoi("0") == 0)
assert(atoi("99999999999999999999999999999999999") == 99999999999999999999999999999999999L)


