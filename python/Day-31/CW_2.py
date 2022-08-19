def gcd(A, B):
    B, A = sorted([abs(A), abs(B)])
    if B == 0:
        return A
    return gcd(B, A % B)


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer

    def solve(self, A, B, C):
        LCM = (B * C) // gcd(B, C)

        return A // LCM
