import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def dfs(self, i, j):
        for dx, dy in self.dir_mat:
            if (
                -1 < i + dx < self.N
                and -1 < j + dy < self.M
                and self.A[i + dx][j + dy] == "X"
            ):
                self.A[i + dx][j + dy] = "O"
                self.dfs(i + dx, j + dy)

    def black(self, A):
        self.A = [list(row) for row in A]
        self.N = len(self.A)
        self.M = len(self.A[0])
        self.dir_mat = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        count = 0

        for i in range(self.N):
            for j in range(self.M):
                if self.A[i][j] == "X":
                    count += 1
                    self.A[i][j] = "O"
                    self.dfs(i, j)

        return count
