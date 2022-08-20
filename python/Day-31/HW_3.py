class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def getFinal(self, A, B):
        B, A = sorted([abs(A), abs(B)])
        if B == 0:
            return A
        if A % B == 0:
            return 2 * B
        return self.getFinal(B, A % B)
