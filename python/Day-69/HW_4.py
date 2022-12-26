class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        N = len(A)

        dp = [[-5e9 for i in range(3)] for j in range(N+1)]

        for i in range(1, N+1):
            dp[i][0] = max(dp[i-1][0], B * A[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i][0] + C * A[i-1])
            dp[i][2] = max(dp[i-1][2], dp[i][1] + D * A[i-1])
        
        return dp[-1][-1]