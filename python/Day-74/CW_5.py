class Solution:
    # @param A : list of integers
    # @return an integer
    def calc(self, i, j):
        if i >= j:
            return 0

        if j == i + 1:
            return self.A[i] * self.A[i + 1] * self.A[i + 2]

        if self.dp[i][j] == -1:
            self.dp[i][j] = float("inf")
            for k in range(i, j):
                self.dp[i][j] = min(
                    self.dp[i][j],
                    self.calc(i, k)
                    + self.calc(k + 1, j)
                    + self.A[i] * self.A[k + 1] * self.A[j + 1],
                )

        return self.dp[i][j]

    def solve(self, A):
        N = len(A) - 1
        self.A = A

        self.dp = [[-1] * (N) for _ in range(N)]

        return self.calc(0, N - 1)
