class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def ed(self, i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if self.dp[i][j] == -1:
            if A[i] == B[j]:
                self.dp[i][j] = self.ed(i - 1, j - 1)
            else:
                self.dp[i][j] = 1 + min(
                    self.ed(i, j - 1), self.ed(i - 1, j), self.ed(i - 1, j - 1)
                )

        return self.dp[i][j]

    def minDistance(self, A, B):
        N = len(A)
        M = len(B)
        self.dp = [[-1] * M for i in range(N)]
        return ed(N - 1, M - 1)
