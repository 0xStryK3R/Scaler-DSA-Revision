class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        # ans = (A//C + int(bool(A%C))) * (B//C + int(bool(B%C)))

        return (-A // C) * (-B // C)
