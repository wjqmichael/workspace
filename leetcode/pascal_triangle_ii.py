class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        rt = []
        for i in xrange(rowIndex + 1): 
            for j in reversed(xrange(1, i)):
                rt[j] = rt[j] + rt[j - 1]
            rt.append(1)
        return rt