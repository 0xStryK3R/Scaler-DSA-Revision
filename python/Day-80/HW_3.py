class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return a list of integers
    def solve(self, p1, p2, p3, k):
        x = 0
        y = 0
        z = 0
        ans = [0] * (k + 1)
        ans[0] = 1
        for i in range(1, k + 1):
            temp = min(min(p1 * ans[x], p2 * ans[y]), p3 * ans[z])
            ans[i] = temp
            if temp == p1 * ans[x]:
                x += 1
            if temp == p2 * ans[y]:
                y += 1
            if temp == p3 * ans[z]:
                z += 1
        ans = ans[1:]
        return ans
