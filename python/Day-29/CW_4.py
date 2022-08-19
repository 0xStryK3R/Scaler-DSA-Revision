class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        N = len(A)
        B = [A[i] + i for i in range(N)]
        C = [A[i] - i for i in range(N)]

        return max(max(B) - min(B), max(C) - min(C))
