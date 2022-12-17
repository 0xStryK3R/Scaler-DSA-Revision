import heapq

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        heapq.heapify(A)
        cost = 0

        while(len(A) > 1):
            sumx = heapq.heappop(A)+heapq.heappop(A)
            cost += sumx
            heapq.heappush(A,sumx)
        
        return cost
        