class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, A, B):
        B, A = sorted([abs(A), abs(B)])
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def solve(self, A):
        GCD = 0
        for num in A:
            if GCD == 1:
                return 0
            GCD = self.gcd(GCD, num)
        if GCD == 1:
            return 0
        else:
            return -1
