import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def dfs(self, i, j):
        for dx, dy in self.dir_mat:
            if (
                -1 < i + dx < self.N
                and -1 < j + dy < self.M
                and self.A[i + dx][j + dy] == 1
            ):
                self.A[i + dx][j + dy] = 0
                self.dfs(i + dx, j + dy)

    def solve(self, A, B, C, D, E, F):
        A += 1
        B += 1
        grid = [[1] * B for _ in range(A)]
        R2 = D**2

        for i in range(A):
            for j in range(B):
                for x, y in zip(E, F):
                    if (x - i) ** 2 + (y - j) ** 2 <= R2:
                        grid[i][j] = 2

        if grid[0][0] == 2 or grid[-1][-1] == 2:
            return "NO"

        self.N = A
        self.M = B
        self.A = grid
        self.dir_mat = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        self.A[0][0] = 0
        self.dfs(0, 0)

        return "YES" if not self.A[-1][-1] else "NO"
