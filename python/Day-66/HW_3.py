import heapq


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        min_heap = []
        max_heap = []

        for c in C:
            heapq.heappush(min_heap, c)
            heapq.heappush(max_heap, -c)

        ans = [0, 0]
        for _ in range(A):
            next_largest = -heapq.heappop(max_heap)
            next_smallest = heapq.heappop(min_heap)
            ans[0] += next_largest
            ans[1] += next_smallest
            next_largest -= 1
            next_smallest -= 1

            if next_largest:
                heapq.heappush(max_heap, -next_largest)

            if next_smallest:
                heapq.heappush(min_heap, next_smallest)

        return ans
