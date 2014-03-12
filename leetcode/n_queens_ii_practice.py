def total_n_queens(n):
    UPPER = (1 << n) - 1

    def helper(row, ld, rd, counter):
        if row == UPPER:
            counter[0] += 1
            return

        pos = UPPER & (~(row | ld | rd))
        while pos:
            p = pos & (~pos + 1)
            pos -= p
            helper(row + p, (ld + p) << 1, (rd + p) >> 1, counter)

    counter = [0]
    helper(0, 0, 0, counter)
    return counter[0]

assert(total_n_queens(4) == 2)
assert(total_n_queens(8) == 92)