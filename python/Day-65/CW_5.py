import heapq


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max_heap = []
        min_heap = []
        output = []

        for num in A:
            if len(max_heap) == len(min_heap):
                if min_heap and num > min_heap[0]:
                    t = min_heap[0]
                    heapq.heapreplace(min_heap, num)
                    num = t
                heapq.heappush(max_heap, -num)
            else:
                if max_heap and num < -max_heap[0]:
                    t = -max_heap[0]
                    heapq.heapreplace(max_heap, -num)
                    num = t
                heapq.heappush(min_heap, num)
            output.append(-max_heap[0])

        return output
