import sys

sys.setrecursionlimit(10**6)
MOD = 10**9 + 7


class Solution:
    # @param A : integer
    # @return an integer
    def ways(self, n):
        if n < 2:
            return 1

        if self.dp[n] == -1:
            self.dp[n] = 0
            for i in range(n):
                l = i
                r = n - l - 1
                self.dp[n] += self.ways(l) * self.ways(r)
            self.dp[n] %= MOD
        return self.dp[n]

    def chordCnt(self, A):
        self.dp = [-1] * (A + 1)
        return self.ways(A)
