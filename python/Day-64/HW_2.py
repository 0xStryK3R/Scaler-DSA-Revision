import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        min_heap = []

        N = len(A)
        d = A[-1]
        for i in range(N - 1):
            heapq.heappush(min_heap, [A[i] / d, (i, N - 1)])

        for _ in range(B):
            f, (i, j) = heapq.heappop(min_heap)
            new_j = j - 1
            new_f = A[i] / A[new_j]
            heapq.heappush(min_heap, [new_f, (i, new_j)])

        return A[i], A[j]
