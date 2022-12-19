import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        max_heap = []
        A.sort(reverse=True)
        B.sort(reverse=True)

        N = len(A)
        b = B[0]

        for i in range(N):
            c = A[i] + b
            heapq.heappush(max_heap, (-c, (i, 0)))

        output = []
        while len(output) < N:
            c, (i, j) = heapq.heappop(max_heap)
            output.append(-c)
            new_j = j + 1
            if new_j < N:
                new_c = A[i] + B[new_j]
                heapq.heappush(max_heap, (-new_c, (i, new_j)))
        return output
