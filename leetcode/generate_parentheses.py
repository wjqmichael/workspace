def generateParenthesis(n):
    def helper(result, cur, left, right, n):
        if (left == right and left == n): 
            result.append(cur)
            return
        if (left > right): helper(result, cur + ')', left, right + 1, n)
        if (left < n): helper(result, cur + '(', left + 1, right, n)
    result = []
    helper(result, "", 0, 0, n)
    return result

print generateParenthesis(3)