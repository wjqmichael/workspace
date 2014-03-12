def total_n_queens(n):
    class _Counter(object):
        def __init__(self):
            self.data = 0

    def helper(row, ld, rd, valid, counter):
        '''
        ld: left diagonal
        rd: right diagonal
        '''
        if row == valid:
            counter.data += 1
            return
        pos = valid & (~(row | ld | rd))
        while pos:
            p = pos & (-pos)
            pos -= p
            helper(row + p, (ld + p) << 1, (rd + p) >> 1, valid, counter)
   
    valid = (1 << n) - 1 # Valid solution
    counter = _Counter()
    helper(0, 0, 0, valid, counter)

    return counter.data

assert(total_n_queens(4) == 2)
assert(total_n_queens(8) == 92)