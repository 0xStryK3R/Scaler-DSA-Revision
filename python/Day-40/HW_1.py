class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, a, b, c):
        n = len(a)
        m = len(b)
        l = 0
        r = m - 1
        dif = 2e9
        ans = [-1, -1]
        ind = [-1, -1]
        while l < n and r >= 0:
            if abs(a[l] + b[r] - c) < dif:
                dif = abs(a[l] + b[r] - c)
                ans[0] = a[l]
                ans[1] = b[r]
                ind[0] = l
                ind[1] = r
            elif abs(a[l] + b[r] - c) == dif:
                if l == ind[0]:
                    ans[0] = a[l]
                    ans[1] = b[r]
                    ind[1] = r

            if a[l] + b[r] >= c:
                r -= 1
            else:
                l += 1
        return ans
