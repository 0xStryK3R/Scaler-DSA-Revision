class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        sum_A = sum(A)
        if sum_A & 1:
            return "No"
        return "Yes"
