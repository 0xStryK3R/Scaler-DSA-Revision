import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        input_data = list(zip(A, B))
        input_data.sort()

        curTime = 0
        pq = []

        for t, p in input_data:
            # if we can buy the ith car
            if t > curTime:
                heapq.heappush(pq, p)
                curTime += 1
            else:
                heapq.heapreplace(pq, max(pq[0], p))

        return sum(pq) % (10**9 + 7)
