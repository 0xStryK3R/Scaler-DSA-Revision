class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        ans = 0

        while A:
            ans += A // 5
            A = A // 5

        return ans
