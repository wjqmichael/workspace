def gray_code(n):
    '''
    Recursive solution. Easy to understand
    '''
    if n == 1:
        return ['0', '1']
    previous = gray_code(n - 1)
    return ['0' + i for i in previous] + ['1' + i for i in reversed(previous)]

print gray_code(4)