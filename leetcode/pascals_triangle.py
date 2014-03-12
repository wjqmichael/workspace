class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if not numRows: return []
        rt = [[1]]
        for i in xrange(numRows - 1):
            new_row = [1]
            last_row = rt[-1]
            for j in xrange(1, len(last_row)):
                new_row.append(last_row[j - 1] + last_row[j])
            new_row.append(1)
            rt.append(new_row)
        return rt