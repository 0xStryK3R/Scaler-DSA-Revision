import heapq


def check_median(A):
    N = len(A)
    max_heap = []
    min_heap = []
    output = []

    for i in range(N - 1):
        num = A[i]
        if len(max_heap) == len(min_heap):
            if min_heap and num > min_heap[0]:
                t = min_heap[0]
                heapq.heapreplace(min_heap, num)
                num = t
            heapq.heappush(max_heap, -num)
            cur_median = -max_heap[0]
        else:
            if max_heap and num < -max_heap[0]:
                t = -max_heap[0]
                heapq.heapreplace(max_heap, -num)
                num = t
            heapq.heappush(min_heap, num)
            cur_median = (-max_heap[0] + min_heap[0]) / 2

        if i and cur_median == A[i + 1]:
            return 1
    return 0


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        return check_median(A) or check_median(A[::-1])
