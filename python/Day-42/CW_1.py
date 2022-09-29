class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        N = len(A)
        max_duplicate_count = 1
        duplicate_count = 1
        for i in range(1, N):
            if A[i] == A[i - 1]:
                duplicate_count += 1
                max_duplicate_count = max(max_duplicate_count, duplicate_count)
            else:
                duplicate_count = 1

        return max_duplicate_count
