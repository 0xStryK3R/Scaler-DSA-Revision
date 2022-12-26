class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        N = len(A[0])
        dp = [-1] * (N)
        dp[0] = max(A[0][0], A[1][0])
        if N > 1:
            dp[1] = max(dp[0], max(A[0][1], A[1][1]))

        for i in range(2, N):
            dp[i] = max(dp[i - 1], max(A[0][i], A[1][i]) + dp[i - 2])

        return dp[-1]
