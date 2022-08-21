class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        l, r = 0, A

        while l <= r:
            mid = (l + r) >> 1
            if (mid * (mid + 1)) >> 1 <= A:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
