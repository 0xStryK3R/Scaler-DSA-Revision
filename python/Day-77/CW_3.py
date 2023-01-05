class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        M = len(A[0])

        DIR_MAT = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        rotten_queue = []
        good_count = 0

        for i in range(N):
            for j in range(M):
                if A[i][j] == 2:
                    rotten_queue.append((i, j))
                if A[i][j] == 1:
                    good_count += 1

        ans = 0

        while good_count and rotten_queue:
            next_queue = []
            for i, j in rotten_queue:
                for dx, dy in DIR_MAT:
                    if -1 < i + dx < N and -1 < j + dy < M and A[i + dx][j + dy] == 1:
                        A[i + dx][j + dy] = 2
                        next_queue.append((i + dx, j + dy))
                        good_count -= 1
            ans += 1
            rotten_queue = next_queue

        if good_count:
            return -1

        return ans
