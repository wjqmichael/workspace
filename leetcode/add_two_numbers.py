def add(l1, l2):
	len_l1 = len(l1)
	len_l2 = len(l2)
	max_len = max(len_l1, len_l2)
	carry = 0
	result = []
	for i in range(max_len):
		n1 = 0 if len_l1 <= i else l1[i]
		n2 = 0 if len_l2 <= i else l2[i]
		sum = n1 + n2 + carry
		carry = 0
		if sum >= 10:
			carry = 1
			sum -= 10
		result.append(sum)
	if carry:
		result.append(carry)
	return result

print add([2, 4, 3], [5, 6, 4])
print add([2, 4, 3], [5, 6, 9])
