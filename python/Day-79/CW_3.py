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

    def solve(self, A, B):
        self.vis = [0] * A
        self.colour = [0] * A

        self.dir_map = {}
        for u, v in B:
            self.dir_map.setdefault(u, set())
            self.dir_map.setdefault(v, set())
            self.dir_map[u].add(v)
            self.dir_map[v].add(u)

        for i in range(A):
            if not self.vis[i]:
                if not self.dfs(i, 1):
                    return 0

        return 1
