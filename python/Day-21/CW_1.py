class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        min_diff = A[1] - A[0]
        i = 1
        while i < len(A):
            min_diff = min(min_diff, A[i] - A[i - 1])
            i += 1

        return min_diff
