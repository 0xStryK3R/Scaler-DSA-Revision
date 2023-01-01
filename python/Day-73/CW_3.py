class Solution:
	# @param A : string
	# @return an integer
    def calc(self, idx):
        if idx<1:
            return 0

        if self.dp[idx]==-1:
            self.dp[idx] = idx
            for i in range(idx+1):
                ts = self.A[idx-i:idx+1]
                rts = str(ts[::-1])
                if ts == rts:
                    if i==idx:
                        self.dp[idx] = 0
                    else:
                        self.dp[idx] = min(self.dp[idx], self.calc(idx-(i+1)) + 1)
    
        return self.dp[idx]
    
	def minCut(self, A):
        N = len(A)
        self.A = A
        self.dp = [-1]*N
        self.dp[0] = 0
        
        self.calc(N-1)
        return  self.dp[-1]