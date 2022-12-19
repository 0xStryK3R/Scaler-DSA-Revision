import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        output = []
        min_heap = []

        for i in range(B):
            heapq.heappush(min_heap, A[i])

        for i in range(B, len(A)):
            heapq.heappush(min_heap, A[i])
            output.append(heapq.heappop(min_heap))

        while min_heap:
            output.append(heapq.heappop(min_heap))

        return output
