def is_valid(s):
    paren = {'(':')', '[':']', '{':'}'}
    stack = []

    for ch in s:
        if ch in paren:
            stack.append(ch)
        else:
            try:
                match = stack.pop()
                if paren[match] != ch:
                    return False
            except IndexError:
                return False

    return True if len(stack)==0 else False

assert(is_valid('()[]{}'))
assert(is_valid('()'))
assert(is_valid(''))
assert(not is_valid("(]"))
assert(not is_valid("([)]"))