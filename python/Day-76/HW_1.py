class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        dp = [{} for _ in range(N)]
        
        cnt = 0
        for i in range(N):
            for j in range(i):
                cur_diff = A[i] - A[j]
                dp[i][cur_diff] = dp[i].get(cur_diff, 0) + dp[j].get(cur_diff, 0) + 1
                cnt += dp[j].get(cur_diff, 0)
        
        return cnt