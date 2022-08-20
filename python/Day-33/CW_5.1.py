# Pascal's triangle approach to nCr Solution!
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        dp = [[0 for i in range(B + 1)] for j in range(A + 1)]
        for i in range(A + 1):
            for j in range(min(i, B) + 1):
                if j == i or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % C
        return dp[A][B] % C
