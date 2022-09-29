class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        i = 0
        sum_A = A[i]

        if sum_A == B:
            return A[:1]

        j = 1
        sum_A += A[j]

        while i <= j:
            if sum_A > B:
                sum_A -= A[i]
                i += 1
            elif sum_A < B:
                j += 1
                if j == len(A):
                    break
                sum_A += A[j]
            else:
                break

        if sum_A == B:
            return A[i : j + 1]
        else:
            return [-1]
