class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if not A:
            return 1
        if A < 3:
            return A

        return self.solve(A - 1) + self.solve(A - 2) + self.solve(A - 3) + A
