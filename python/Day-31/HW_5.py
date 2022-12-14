class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, A, B):
        B, A = sorted([abs(A), abs(B)])
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def solve(self, A):
        ans = 0
        for num in A:
            ans = self.gcd(ans, num)
        return ans
