class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        MOD = 10**9 + 7
        N, M = len(A), len(A[0])
        Q = len(B)

        A = [[0] * (M)] + A
        A = [list([0]) + row for row in A]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                A[i][j] += A[i][j - 1]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                A[i][j] += A[i - 1][j]
        ans = []

        for i in range(Q):
            x1, y1, x2, y2 = B[i], C[i], D[i], E[i]
            ans.append(
                (A[x2][y2] + A[x1 - 1][y1 - 1] - A[x1 - 1][y2] - A[x2][y1 - 1]) % MOD
            )

        return ans
