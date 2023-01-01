class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        mxval = 50 * n
        dp = [0] * (mxval + 1)
        for i in range(mxval + 1):
            dp[i] = 1e9
        dp[0] = 0

        for i in range(n):
            for val in range(mxval, A[i] - 1, -1):
                dp[val] = min(dp[val], B[i] + dp[val - A[i]])

        ans = 0
        for val in range(mxval, -1, -1):
            if dp[val] <= C:
                ans = val
                break
        return ans
