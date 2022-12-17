import heapq


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        min_heap = []

        N = len(A)
        M = len(A[0])
        for i in range(N):
            heapq.heappush(min_heap, [A[i][0], (i, 0)])

        for _ in range(B):
            val, (i, j) = heapq.heappop(min_heap)
            new_j = j + 1
            if new_j < M:
                new_val = A[i][new_j]
                heapq.heappush(min_heap, [new_val, (i, new_j)])

        return val
