class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sumA = sum(A)
        A.sort()
        sumB1 = sum(A[:B])
        sumB2 = sum(A[-B:])

        return max(abs(2 * sumB1 - sumA), abs(2 * sumB2 - sumA))
