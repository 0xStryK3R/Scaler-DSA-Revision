class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        N = len(A)
        dp = [0] * N

        rev = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for i in range(1, N):
            if A[i] in rev:
                x = dp[i - 1]
                prev_idx = i - x - 1
                if prev_idx > -1 and A[prev_idx] == rev[A[i]]:
                    dp[i] = x + 2
                    if i > x + 1:
                        dp[i] += dp[i - 2 - x]

        return max(dp)
