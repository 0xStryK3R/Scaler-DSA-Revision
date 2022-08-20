class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        B, A = sorted([abs(A), abs(B)])
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def cpFact(self, A, B):
        while self.gcd(A, B) > 1:
            A //= self.gcd(A, B)
        return A
