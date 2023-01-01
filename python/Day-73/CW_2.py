class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        if n == 1:
            return A

        dp = [[False] * n for _ in range(n)]
        dp[-1][-1] = True

        for i in range(n - 1):
            dp[i][i] = True
            if A[i] == A[i + 1]:
                dp[i][i + 1] = True

        ans = ""
        for i in range(2, n + 1):
            for j in range(n - i + 1):
                if dp[j + 1][i + j - 2] and A[j] == A[i + j - 1]:
                    dp[j][i + j - 1] = True

        max_len = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    max_len = max(j - i + 1, max_len)

        for i in range(n):
            for j in range(n):
                if dp[i][j] and j - i + 1 == max_len:
                    return A[i : j + 1]
