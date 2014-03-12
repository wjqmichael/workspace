'''
Given: 
- integer array [-3, 0, 1, 2, -5, 6, 2, 0]
- start index i into the array
- end index j into the array
- i <= j

Find: the sum of the elements between i and j, inclusive.
Example:
i = 2
j = 5
return 1 + 2 + (-5) + 6 = 4

Assumptions:
- array does not change
- many requests for the sum between different i's and j's.
'''

class SubSum(object):
    def __init__(self, array):
        self.array = array
        self.sum_ends = self.get_sum_ends(array)

    def get_sum_ends(self, array):
        if not array:
            return None
        rt = [array[0]]
        for i in array[1:]:
            rt.append(i + rt[-1])
        return rt

    def sub_sum(self, i, j):
        if not self.sum_ends or i > j:
            return 0
        return self.sum_ends[j] - (self.sum_ends[i - 1] if i > 0 else 0)

ss = SubSum([-3, 0, 1, 2, -5, 6, 2, 0])
print ss.sub_sum(2, 5)
