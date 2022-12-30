class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        prev_row = [0] * len(A[0])
        prev_val = 1

        for i, cur_row in enumerate(A):
            for j, pos in enumerate(cur_row):
                if pos & 1:
                    prev_row[j] = 0
                    prev_val = 0
                else:
                    prev_row[j] += prev_val
                    prev_val = prev_row[j]
            prev_val = 0

        return prev_row[-1]
