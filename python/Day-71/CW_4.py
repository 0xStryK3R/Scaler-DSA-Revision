class Solution:
	# @param A : tuple of integers
	# @return an integer
    def calc(self, idx):
        if idx<0:
            return 0
    
        if not self.dp[idx]:
            for i in range(idx):
                x = self.calc(i)
                if self.A[i]<self.A[idx]:
                    self.dp[idx] = max(x, self.dp[idx])
            self.dp[idx] += 1
        return self.dp[idx]
    
    def lis(self, A):
        self.A = A
        N = len(A)
        self.dp = [0]*N
        
        self.calc(N-1)
        return max(self.dp)
