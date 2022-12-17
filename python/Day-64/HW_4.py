import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heapq.heapify(A)
        eaten = 0

        while A[0] <= B:
            nxt = heapq.heappop(A)
            eaten += nxt >> 1
            nxt -= nxt >> 1
            if not A:
                break
            heapq.heapreplace(A, A[0] + nxt)

        return eaten
