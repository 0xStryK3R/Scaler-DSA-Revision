class Solution:
    # @param A : integer
    # @return an integer
    def countMinSquares(self, A):
        dp = list(range(A + 1))
        for i in range(2, A + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j])
                j += 1
            dp[i] += 1
        return dp[A]
