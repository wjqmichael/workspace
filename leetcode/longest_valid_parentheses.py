def longest_valid_parentheses(s):
    '''
    This algorithm is done in one time pass and for every index,
    it checks 'the longest valid string that ends at that index'. 
    '''
    stack = []
    lst = -1
    max_len = 0
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        else:
            if len(stack):
                stack.pop()
                if len(stack):
                    max_len = max(max_len, i - stack[-1])
                else:
                    max_len = max(max_len, i - lst)
            else:
                lst = i
    return max_len

assert(longest_valid_parentheses("()") == 2)
assert(longest_valid_parentheses("") == 0)
assert(longest_valid_parentheses("(") == 0)
assert(longest_valid_parentheses(")") == 0)
assert(longest_valid_parentheses("((()") == 2)
assert(longest_valid_parentheses("))()())") == 4)