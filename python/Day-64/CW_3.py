import heapq


def prod(arr):
    ans = 1
    for num in arr:
        ans *= num
    return ans


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        min_heap = []
        output = []

        for num in A:
            if len(min_heap) < 3:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heapreplace(min_heap, num)

            output.append(prod(min_heap) if len(min_heap) > 2 else -1)

        return output
