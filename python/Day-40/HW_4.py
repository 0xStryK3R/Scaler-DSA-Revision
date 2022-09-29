class Solution:
    # @param A : list of integers
    # @return an integer
    def get_subarr_count(self, l, r, x):
        n = r - l
        cnt = (n * (n + 1)) // 2
        if x:
            m = x - l
            cnt -= (m * (m + 1)) // 2
        return cnt

    def solve(self, A):
        N = len(A)
        hash_A = {A[0]: 0}
        l = 0
        r = 1
        x = 0
        ans = 0

        while r < N:
            if A[r] in hash_A:
                if hash_A[A[r]] >= l:
                    ans += self.get_subarr_count(l, r, x)
                    l = hash_A[A[r]] + 1
                    x = r
            hash_A[A[r]] = r
            r += 1

        ans += self.get_subarr_count(l, r, x)

        return ans % (10**9 + 7)
