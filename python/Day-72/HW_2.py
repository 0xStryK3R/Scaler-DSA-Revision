class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def match(self, i, j):
        if j < 0:
            return 1

        if i < 0:
            return 0

        if self.dp[i][j] == -1:
            self.dp[i][j] = self.match(i - 1, j)
            if self.A[i] == self.B[j]:
                self.dp[i][j] += self.match(i - 1, j - 1)

        return self.dp[i][j]

    def numDistinct(self, A, B):
        self.A = A
        self.B = B
        N = len(A)
        M = len(B)

        self.dp = [[-1] * M for _ in range(N)]

        return int(self.match(N - 1, M - 1))
