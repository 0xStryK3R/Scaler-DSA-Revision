class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        N = len(A)
        min_distance = N
        distance_map = {}

        for i, num in enumerate(A):
            if num in distance_map:
                min_distance = min(min_distance, i - distance_map[num])

            distance_map[num] = i

        if min_distance == N:
            min_distance = -1
        return min_distance
