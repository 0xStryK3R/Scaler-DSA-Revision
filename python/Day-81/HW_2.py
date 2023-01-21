MOD = 1e9 + 7


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        M = len(B)
        edge_wts = []
        for i in range(N):
            edge_wts.append([A[i], 0])
        for i in range(M):
            edge_wts.append([B[i], 1])
        edge_wts.sort()
        N += 1
        M += 1
        ans = 0
        for w, d in edge_wts:
            if not d:
                ans += M * w
                N -= 1
            else:
                ans += N * w
                M -= 1
            ans %= MOD
        return int(ans)
