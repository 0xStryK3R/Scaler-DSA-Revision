class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        MOD = 10**9 + 7
        i, j = 0, len(A) - 1
        valid_rect = 0

        while i <= j:
            if A[i] * A[j] < B:
                valid_rect = (valid_rect + 2 * (j - i) + 1) % MOD
                i += 1
            else:
                j -= 1
        return valid_rect
