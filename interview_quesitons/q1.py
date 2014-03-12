'''
C={1,2,2,3,4,5} 
Sum=5 

subset; 
{1,2,2} 
{1,4} 
{2,3} 
'''

def find_subsets(a, target_sum):
    def helper(ind, remain_sum, rt, current):
        for i, num in enumerate(a[ind:]):
            if num > remain_sum:
                return
            if num == remain_sum:
                rt.add(tuple(current + [num]))
                return
            current.append(num)
            helper(i + 1, remain_sum - num, rt, current)
            current.pop(-1)
    rt = set()
    current = []
    helper(0, target_sum, rt, current)
    return rt

# print find_subsets([2,2,3], 5)
print find_subsets([1,2,2,3,4,5], 5)