class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        MOD = 10**9 + 7
        A -= B + C + D - 2

        return ((A * (A - 1)) >> 1) % MOD
