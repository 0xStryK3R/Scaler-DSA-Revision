class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        numerator = denominator = 1
        B = min(B, A - B)
        for i in range(B):
            numerator *= A - B + 1 + i
            denominator *= i + 1
        # denominator = self.pow(denominator, C-2, C)

        return (numerator // denominator) % C
