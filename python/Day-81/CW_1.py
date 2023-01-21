class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def find(self, x):
        if self.P[x] != x:
            self.P[x] = self.find(self.P[x])
        return self.P[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.P[x] = y
        return

    def solve(self, A, B, C, D):
        self.P = list(range(A))
        for u, v in C:
            self.union(u - 1, v - 1)

        for i in range(A):
            self.find(i)

        cc_map = {}

        for i, p in enumerate(self.P):
            cc_map[p] = cc_map.get(p, 0) + B[i]

        count = 0

        for cc, strength in cc_map.items():
            if strength >= D:
                count += 1

        return count
