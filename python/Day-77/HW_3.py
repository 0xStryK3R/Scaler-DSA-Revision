class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        M = len(A[0])
        DIR_MAT = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        B = [[None] * M for _ in range(N)]

        queue = []

        for i in range(N):
            for j in range(M):
                if A[i][j] == 1:
                    queue.append((i, j))
                    B[i][j] = 0

        level = 0
        while queue:
            level += 1
            next_queue = []
            for i, j in queue:
                for dx, dy in DIR_MAT:
                    if (
                        -1 < i + dx < N
                        and -1 < j + dy < M
                        and B[i + dx][j + dy] == None
                    ):
                        B[i + dx][j + dy] = level
                        next_queue.append((i + dx, j + dy))
            queue = next_queue

        return B
