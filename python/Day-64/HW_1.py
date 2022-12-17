import heapq


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        dist_heap = []

        for x, y in A:
            dist = x**2 + y**2
            heapq.heappush(dist_heap, [dist, (x, y)])

        output = []

        for _ in range(B):
            output.append(heapq.heappop(dist_heap)[1])

        return output
