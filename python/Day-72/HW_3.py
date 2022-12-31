class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B = str(A[::-1])
        N = len(A)
        M = len(B)
        
        dp = [[0] + [False for j in range(M)] for i in range(N+1)]
        
        dp[0] = [0]*(M+1)
        for i in range(1, N+1):
            for j in range(1, M+1):
                if A[i-1]==B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[N][M]