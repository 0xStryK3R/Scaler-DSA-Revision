class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 2:
            return A[0][0] * A[1][1] - A[1][0] * A[0][1]
        if len(A) == 3:
            return (
                A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
                - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
                + A[0][2] * (A[1][0] * A[2][1] - A[2][0] * A[1][1])
            )
