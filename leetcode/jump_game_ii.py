import sys

def jump(A):
    ''' using dynamic programming, which is actually an overkill'''
    least_jmp = [sys.maxint] * len(A)
    least_jmp[-1] = 0
    for i in xrange(len(A) - 2, -1, -1):
        end = min(i + A[i], len(A) - 1)
        relay = min(least_jmp[i + 1:end + 1])
        if relay != sys.maxint:
            least_jmp[i] = relay + 1
    return least_jmp[0]

def jump_linear_solution(A):
    num_jump = 0
    curr = 0
    reach = 0
    for i in xrange(len(A)):
        if i > curr:
            num_jump += 1
            curr = reach
        reach = max(reach, i + A[i])
    return num_jump
    

print(jump([2,3,1,1,4]))
print(jump_linear_solution([2,3,1,1,4]))
