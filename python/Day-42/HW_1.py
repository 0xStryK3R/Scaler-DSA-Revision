class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        chunk_count = 0
        N = len(A)
        max_in_range = -1
        min_in_range = 0
        min_found = False

        for i in range(N):
            max_in_range = max(A[i], max_in_range)

            if A[i] == min_in_range:
                min_found = True

            if min_found and i >= max_in_range:
                min_found = False
                chunk_count += 1
                min_in_range = i + 1
                max_in_range = i

        return chunk_count
