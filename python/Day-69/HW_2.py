class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        n = len(A)
        imax = imin = max_prod = A[0]
        for i in range(1, n):
            imin, _, imax = sorted([A[i], imax * A[i], imin * A[i]])
            max_prod = max(max_prod, imax)
        return max_prod
