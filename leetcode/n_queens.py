from copy import deepcopy
from math import log

def solve_n_queens(n):
    upper = (1 << n) - 1
    board = [['.'] * n for i in xrange(n)]
    rt = []

    def helper(row, ld, rd, curr_row):
        if row == upper:
            rt.append(deepcopy(board))
            return

        positions = upper & ~(row | ld | rd)
        while positions:
            p = positions & (-positions)
            ind = int(log(p, 2))
            board[curr_row][ind] = 'Q'
            helper(row + p, (ld + p) << 1, (rd + p) >> 1, curr_row + 1)
            board[curr_row][ind] = '.'
            positions -= p

    helper(0, 0, 0, 0)
    return rt

print solve_n_queens(4)