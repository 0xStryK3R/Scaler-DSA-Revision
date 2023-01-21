class CC:
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

    def solve(self, A, C):
        self.P = list(range(A))
        for u, v in C:
            self.union(u - 1, v - 1)

        for i in range(A):
            self.find(i)

        cc_set = set()
        cc_count = 0

        for p in self.P:
            if p not in cc_set:
                cc_set.add(p)
                cc_count += 1

        return cc_count


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):
        MOD = 10**9 + 7
        b = list(zip(*B))
        c = list(zip(*C))

        if set(set(b[0]) | set(b[1])) & set(set(c[0]) | set(c[1])):
            return 0

        B += C
        cc_count = CC().solve(A, B)
        return (2**cc_count) % MOD
