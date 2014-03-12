class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        while n > 0:
            if m >= 1 and A[m - 1] > B[n - 1]:
                A[n + m - 1] = A[m - 1]
                m -= 1
            else:
                A[n + m - 1] = B[n - 1]
                n -= 1