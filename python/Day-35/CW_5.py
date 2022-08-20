class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        ans = 0
        for i in range(32):
            ans = ans << 1 + (A & (1 << i)) >> i
        return ans
