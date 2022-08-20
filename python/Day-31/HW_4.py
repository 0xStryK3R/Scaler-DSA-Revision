class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, A, B):
        B, A = sorted([abs(A), abs(B)])
        if B == 0:
            return A
        return self.gcd(B, A % B)

    def solve(self, A):
        # If GCD = 1, there exists atleast 1 subsequence of numbers which has zero common divisors
        # between the numbers in that subsequence. And since, each number contributes only once
        # towards its divisors frequency, and none of the divisors frequency will ever match subsequence
        # size in this particular case, loop will break and return 1 at end.
        ans = 0
        for num in A:
            ans = self.gcd(ans, num)
        return int(ans == 1)
