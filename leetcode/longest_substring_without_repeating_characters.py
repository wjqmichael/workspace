'''
Given a string, find the length of the longest substring
without repeating characters. For example, the longest 
substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", 
with the length of 1.
'''


import string


def getLongestLen(s):
	counter = dict(zip(string.lowercase, [False] * 26))
	cursor = 0
	start = 0
	current_len = 0
	max_len = 0
	while (cursor < len(s)):
		c = s[cursor]
		if counter[c]:
			cursor = start = s.find(c, start) + 1
			counter = dict(zip(string.lowercase, [False] * 26))
			if current_len > max_len:
				max_len = current_len
			current_len = 0
		else:
			counter[c] = True
			cursor += 1
			current_len += 1
	return max_len


assert(getLongestLen("otodinokzfhycbuwygqsofctljsgezbvsryceomdvvdyzzuxfnrwstpgejmlkpgegggnuusrswprxmqdzhzrcqzgcltmcz") == 16)
assert(getLongestLen("inprobabilitytheoryandstatisticsamedianisdescribedasthenumericvalueseparating") == 10)
assert(getLongestLen("") == 0)