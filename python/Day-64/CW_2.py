import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heapq.heapify(A)

        for i in range(B):
            heapq.heappush(A, heapq.heappop(A) * -1)

        return sum(A)
