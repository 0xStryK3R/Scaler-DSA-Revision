import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        min_heap = []
        N = len(A)

        for i in range(N):
            num = A[i]
            next_sum = num * 2

            heapq.heappush(min_heap, (next_sum, (i, num)))

        for _ in range(B):
            cur_sum, (i, num) = heapq.heappop(min_heap)
            A[i] = cur_sum
            next_sum = cur_sum + num
            heapq.heappush(min_heap, (next_sum, (i, num)))

        return max(A)
