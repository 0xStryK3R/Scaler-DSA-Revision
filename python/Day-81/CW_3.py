class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False  # Forming a cycle, not added
        self.p[y] = x
        return True  # Added as not in CC

    def solve(self, A, B):
        self.p = list(range(A + 1))
        B.sort(key=lambda x: x[-1])
        ans = 0
        for x, y, w in B:
            if self.union(x, y):
                ans += w
        return ans
