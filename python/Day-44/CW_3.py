class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        hash_x = {}
        hash_y = {}
        N = len(A)
        for i in range(N):
            hash_x.setdefault(A[i], 0)
            hash_x[A[i]] += 1
            hash_y.setdefault(B[i], 0)
            hash_y[B[i]] += 1

        ans = 0
        for i in range(N):
            ans += (hash_x[A[i]] - 1) * (hash_y[B[i]] - 1)

        return ans
