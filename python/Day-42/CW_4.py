class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        MOD = 10**9 + 7
        A.sort()
        N = len(A)
        min_magic_num = 0
        max_magic_num = (sum(A) - 2 * sum(A[: N // 2])) % MOD
        for i in range(N):
            if i & 1:
                min_magic_num = (min_magic_num + A[i]) % MOD
            else:
                min_magic_num -= A[i]

        return max_magic_num, min_magic_num
