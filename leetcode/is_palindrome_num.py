def get_div(num):
	div = 1
	num /= 10
	while num:
		div *= 10
		num /= 10
	return div

def is_panlindrome_num(num):
	if num < 0:
		return False
	div = get_div(num)
	while num:
		l = num / div
		r = num % 10
		if l != r:
			return False
		num = (num % div) / 10
		div /= 100
	return True

assert (is_panlindrome_num(121))
assert (is_panlindrome_num(1234321))
assert (is_panlindrome_num(1))
assert (not is_panlindrome_num(-121))
assert (not is_panlindrome_num(1234311))