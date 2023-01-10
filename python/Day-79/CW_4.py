import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def dfs(self, node, colour=1):
        self.vis[node] = 1
        self.colour[node] = colour
        colour *= -1

        for ch in self.dir_map.get(node, []):
            if not self.vis[ch]:
                if not self.dfs(ch, colour):
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
                if not self.dfs(i, 1):
                    return 0

        return 1

    def solve(self, A, B):
        if not self.check_bipartite(A, B):
            return 0

        u_count = self.colour.count(1)
        v_count = self.colour.count(-1)

        return (u_count * v_count - len(B)) % (10**9 + 7)
