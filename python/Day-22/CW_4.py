class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        return min([A[i + B - 1] - A[i] for i in range(len(A) - B + 1)])
