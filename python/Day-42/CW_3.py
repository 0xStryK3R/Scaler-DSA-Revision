class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        m = 10**9 + 7
        A.sort()
        ans = 0
        N = len(A)
        for i in range(N):
            ans = (ans + (A[i] << i) % m - (A[i] << (N - i - 1)) % m) % m

        return ans
