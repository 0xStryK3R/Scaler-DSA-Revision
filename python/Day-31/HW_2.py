class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        # GCD of 2 consequtive numbers is always 1, so answer will be 1 if A!=B
        if A == B:
            return A
        else:
            return 1
