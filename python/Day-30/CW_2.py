class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N, M = len(A), len(A[0])

        all_submat_sum = 0

        for i in range(N):
            for j in range(M):
                a = cnt_mat_starting_before_xy = (i + 1) * (j + 1)
                b = cnt_mat_endning_after_xy = (N - i) * (M - j)

                all_submat_sum += a * b * A[i][j]

        return all_submat_sum
