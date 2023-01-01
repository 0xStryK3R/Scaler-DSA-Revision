class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        N = len(A)

        dp = [[0] + [-1] * D for _ in range(N + 1)]
        dp[0] = [0] * (D + 1)

        for i in range(1, N + 1):
            for j in range(1, D + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    j >= C[i - 1] and (A[i - 1] * B[i - 1] + dp[i][j - C[i - 1]]),
                )

        return dp[-1][-1]
