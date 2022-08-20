class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        N = len(A)
        A.sort()

        # XOR of two numbers minimises as they approach each
        # other and become zero when they are equal.

        ans = A[0] ^ A[1]
        for i in range(2, N):
            ans = min(ans, A[i - 1] ^ A[i])
        return ans
