class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        prev_row = [10**9] * len(A[0])
        prev_val = 0
        for i, cur_row in enumerate(A):
            for j, pos in enumerate(cur_row):
                prev_row[j] = pos + min(prev_row[j], prev_val)
                prev_val = prev_row[j]
            prev_val = prev_row[0]

        return prev_row[-1]
