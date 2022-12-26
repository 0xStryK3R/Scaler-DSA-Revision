import sys
sys.setrecursionlimit(10**6)

class Solution:
    # @param A : integer
    # @return an integer
    def __init__(self):
        self.dp = [-1]*100000
        self.dp[0] = self.dp[1] = 1
        
    def climbStairs(self, A):
        if self.dp[A]==-1:
            self.dp[A] = self.climbStairs(A-1) + self.climbStairs(A-2)
        
        return self.dp[A]%(10**9+7)