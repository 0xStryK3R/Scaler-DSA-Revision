class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        N = len(A)

        b_max = c_max = d_max = -5e9

        for i in range(1, N + 1):
            b_max = max(b_max, B * A[i - 1])
            c_max = max(c_max, b_max + C * A[i - 1])
            d_max = max(d_max, c_max + D * A[i - 1])

        return d_max
