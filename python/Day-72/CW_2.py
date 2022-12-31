class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def isMatch(self, s, p):
        A = 'a'+ s #Padding to handle base case
        B = 'a' + p #Padding to handle base case
        N = len(A)
        M = len(B)
        
        dp = [[False]*(M+1) for i in range(N+1)]
        dp[0][0] = True
        
        for i in range(1, N+1):
            for j in range(1, M+1):
                if A[i-1]==B[j-1] or B[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif B[j-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        
        return int(dp[N][M])