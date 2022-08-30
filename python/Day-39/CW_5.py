DIR_MAT = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def walk(self, x, y, zeroes, tab=""):
        if not zeroes:
            if self.A[x][y] == 2:
                self.ans += 1
            return

        if self.A[x][y] == 2:
            return

        val = self.A[x][y]
        self.A[x][y] = -1
        for dx, dy in DIR_MAT:
            if (
                -1 < x + dx < self.N
                and (-1 < y + dy < self.M)
                and (self.A[x + dx][y + dy] in (0, 2))
            ):
                self.walk(x + dx, y + dy, zeroes - 1, tab + ">")
        self.A[x][y] = val

    def solve(self, A):
        N, M = len(A), len(A[0])
        zeroes = 1

        for i in range(N):
            for j in range(M):
                if A[i][j] == 0:
                    zeroes += 1
                if A[i][j] == 1:
                    x, y = i, j

        self.A = A
        self.N = N
        self.M = M
        self.ans = 0

        self.walk(x, y, zeroes)

        return self.ans
