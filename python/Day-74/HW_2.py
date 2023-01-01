INF = 10000000

dp = []

class Solution:
    def solve(self, A, B, C):

        dp = [[0 for i in range(1005)] for j in range(1005)]

        dish = []
        n = len(C)

        for i in range(n):
            dish.append([B[i], C[i]])

        m = max(A)

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = INF
                else:
                    if i >= dish[j - 1][0]:
                        dp[i][j] = min(
                            dp[i][j - 1], dp[i - dish[j - 1][0]][j] + dish[j - 1][1]
                        )
                    else:
                        dp[i][j] = dp[i][j - 1]

        ans = 0
        for i in range(len(A)):
            ans += dp[A[i]][n]

        return ans