MOD = 10**9 + 7


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def get_count(self, N, S):
        if N == 1:
            return int(0 < S < 10)

        if self.dp[N][S] == -1:
            self.dp[N][S] = 0
            for num in range(10):
                if S - num < 0 or S > 9 * N:
                    break
                self.dp[N][S] += self.get_count(N - 1, S - num)

        self.dp[N][S] %= MOD

        return self.dp[N][S]

    def solve(self, A, B):
        self.dp = [[-1] * (B + 1) for _ in range(A + 1)]
        return int(self.get_count(A, B))
