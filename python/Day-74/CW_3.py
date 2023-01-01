class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        N = len(B)
        dp = [[0] + [-1] * A for i in range(N + 1)]
        dp[0] = [0] * (A + 1)

        for i in range(1, N + 1):
            for j in range(1, A + 1):
                dp[i][j] = max(
                    dp[i - 1][j], j >= C[i - 1] and (B[i - 1] + dp[i][j - C[i - 1]])
                )

        return dp[-1][-1]
