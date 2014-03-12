def word_search(board, word):
    def helper(r, c, word):
        if not word: return True
        # Up
        if r and board[r - 1][c] == word[0]:
            if helper2(r, c, r - 1, c, word): return True

        # Down
        if r < len(board) - 1 and board[r + 1][c] == word[0]:
            if helper2(r, c, r + 1, c, word): return True

        # Left
        if c and board[r][c - 1] == word[0]:
            if helper2(r, c, r, c - 1, word): return True

        # Right
        if c < len(board[0]) - 1 and board[r][c + 1] == word[0]:
            if helper2(r, c, r, c + 1, word): return True

    def helper2(r, c, nr, nc, word):
        ch = board[r][c]
        board[r][c] = '#'
        rt = False
        if helper(nr, nc, word[1:]): 
            rt = True
        board[r][c] = ch
        return rt
    
    if not word: return True
    if not len(board) or not len(board[0]): return False

    for r in xrange(len(board)):
        for c in xrange(len(board[0])):
            if board[r][c] == word[0] and helper(r, c, word[1:]): return True
    return False

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

print word_search(board, 'ABCCED')
print word_search(board, 'SEE')
print word_search(board, 'ABCB')
print board