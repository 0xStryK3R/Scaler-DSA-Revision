class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        rows = len(A)
        cols = len(A[0])
        dp = [[1000000000000 for x in range(cols + 1)] for x in range(rows + 1)]
        dp[rows - 1][cols] = 1
        dp[rows][cols - 1] = 1
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                need = min(dp[i][j + 1], dp[i + 1][j]) - A[i][j]
                dp[i][j] = 1 if need <= 0 else need
        return dp[0][0]
