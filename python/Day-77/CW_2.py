import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def dfs(self, i, j):
        for dx, dy in self.dir_mat:
            if -1 < i + dx < self.N and -1 < j + dy < self.M and self.A[i + dx][j + dy]:
                self.A[i + dx][j + dy] = 0
                self.dfs(i + dx, j + dy)

    def solve(self, A):
        self.N = len(A)
        self.M = len(A[0])
        self.A = A
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
        count = 0

        for i in range(self.N):
            for j in range(self.M):
                if self.A[i][j]:
                    count += 1
                    self.A[i][j] = 0
                    self.dfs(i, j)

        return count
