class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        N = len(A)
        M = len(A[0])

        DIR_MAT = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        queue = set()

        for i in [0, N - 1]:
            for j in range(M):
                if A[i][j] == "O":
                    queue.add((i, j))

        for i in range(N):
            for j in [0, M - 1]:
                if A[i][j] == "O":
                    queue.add((i, j))

        boundary_Os = set()
        while queue:
            boundary_Os |= queue
            next_queue = set()
            for i, j in queue:
                for dx, dy in DIR_MAT:
                    if -1 < i + dx < N and -1 < j + dy < M and A[i + dx][j + dy] == "O":
                        A[i + dx] = (
                            "".join(A[i + dx][: j + dy])
                            + "X"
                            + "".join(A[i + dx][j + dy + 1 :])
                        )
                        next_queue.add((i + dx, j + dy))
            queue = next_queue

        for i in range(N):
            A[i] = "X" * M

        for i, j in boundary_Os:
            A[i] = "".join(A[i][:j]) + "O" + "".join(A[i][j + 1 :])
