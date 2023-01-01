class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        N = len(A)
        prev_row = [0] * (C + 1)
        cur_row = [0] + [-1] * C

        for i in range(1, N + 1):
            for j in range(1, C + 1):
                cur_row[j] = max(
                    prev_row[j], j >= B[i - 1] and (A[i - 1] + prev_row[j - B[i - 1]])
                )
            prev_row = cur_row[:]

        return cur_row[-1]
