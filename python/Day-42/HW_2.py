class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        swap_cnt = 0
        for i in range(len(A)):
            while A[i] != i:
                t = A[A[i]]
                A[A[i]] = A[i]
                A[i] = t
                swap_cnt += 1

        return swap_cnt
