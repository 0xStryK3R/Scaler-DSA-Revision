class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        min_diff = abs(A[0] - A[-1])
        for i in range(1, len(A)):
            min_diff = min(min_diff, abs(A[i] - A[i - 1]))
        return min_diff
