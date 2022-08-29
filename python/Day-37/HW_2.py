class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        l = ans = 0
        r = A
        while l <= r:
            m = (l + r) >> 1
            if m * m > A:
                r = m - 1
            else:
                ans = m
                l = m + 1

        return ans
