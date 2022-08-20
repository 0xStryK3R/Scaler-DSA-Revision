class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if C == 1:
            return 0
        numerator = denominator = 1
        B = min(B, A - B)
        for i in range(B):
            numerator = (numerator * (A - i)) % C
            denominator = (denominator * (i + 1)) % C

        return (numerator * pow(denominator, C - 2, C)) % C
