class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        i = 1

        while A >> (i - 1):
            if (A >> (i - 1)) & 1:
                ans += 5**i
            i += 1

        return ans
