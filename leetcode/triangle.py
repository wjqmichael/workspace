class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return None
        min_sum = [triangle[0][0]]
        for row in triangle[1:]:
            tmp_min_sum = []
            for i, num in enumerate(row):
                neighbors = []
                if i < len(row) - 1:
                    neighbors.append(min_sum[i])
                if i >= 1:
                    neighbors.append(min_sum[i - 1])
                tmp_min_sum.append(min(neighbors) + num)
            min_sum = tmp_min_sum
        return min(min_sum)