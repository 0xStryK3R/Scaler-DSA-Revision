class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        while A & (A - 1):
            A &= A - 1

        return A
