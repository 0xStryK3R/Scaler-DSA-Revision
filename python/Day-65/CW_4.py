import heapq

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        min_heap = []
        output = []

        for num in B:
            if len(min_heap) < A:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
            output.append(-1 if not len(min_heap)==A else min_heap[0])
        
        return output

