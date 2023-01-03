class Solution:
    # @param A : list of integers
    # @return an integer
    def get_max_prod(self, l, r):
        if l + 1 >= r:
            return 0

        if not self.dp[l][r]:
            max_prod = 0
            for i in range(l + 1, r):
                max_prod = max(
                    max_prod,
                    self.A[l] * self.A[i] * self.A[r]
                    + self.get_max_prod(l, i)
                    + self.get_max_prod(i, r),
                )
            self.dp[l][r] = max_prod

        return self.dp[l][r]

    def solve(self, A):
        A = [1] + A + [1]
        N = len(A)
        if N == 3:
            return A[1]

        if N == 4:
            return A[1] * A[2] + max(A)

        self.A = A
        self.dp = [[0] * (N) for _ in range(N)]

        return self.get_max_prod(0, N - 1)
