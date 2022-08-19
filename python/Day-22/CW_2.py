class Solution:
    # @param A : list of integers
    # # @return an integer
    def solve(self, A):
        MOD = 10**9 + 7

        N = len(A)
        A.sort()

        ans = 0

        for i in range(N):
            num = A[i]
            max_in = (2**i) % MOD
            min_in = (2 ** (N - 1 - i)) % MOD
            ans = (ans + (max_in - min_in) * num) % MOD

        return ans
