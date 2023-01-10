import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def colour_dfs(self, node, colour=1):
        self.vis[node] = 1
        self.colour[node] = colour
        colour *= -1

        for ch in self.dir_map.get(node, []):
            if not self.vis[ch]:
                if not self.colour_dfs(ch, colour):
                    return False
            elif self.colour[node] == self.colour[ch]:
                return False

        return True

    def check_bipartite(self, A, B):
        self.vis = [0] * A
        self.colour = [0] * A

        self.dir_map = {}
        for u, v in B:
            self.dir_map.setdefault(u - 1, set())
            self.dir_map.setdefault(v - 1, set())
            self.dir_map[u - 1].add(v - 1)
            self.dir_map[v - 1].add(u - 1)

        for i in range(A):
            if not self.vis[i]:
                if not self.colour_dfs(i, 1):
                    return 0

        return 1

    def dfs(self, node):
        self.vis[node] = 1
        u = v = 0
        if self.colour[node] == 1:
            u += 1
        else:
            v += 1
        for ch in self.dir_map.get(node, []):
            if not self.vis[ch]:
                a, b = self.dfs(ch)
                u += a
                v += b

        return u, v

    def solve(self, A, B):
        if not self.check_bipartite(A, B):
            return 0

        self.vis = [0] * A
        MOD = 998244353
        ans = 1
        for i in range(A):
            if not self.vis[i]:
                u, v = self.dfs(i)
                ans *= 2**u + 2**v
                ans %= MOD

        return ans
