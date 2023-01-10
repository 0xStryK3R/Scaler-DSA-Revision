import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def dfs(self, node):
        self.nodes[node] = 1
        has_cycle = any(
            [
                ((self.nodes[ch] == 1) or (self.nodes[ch] == 0 and self.dfs(ch)))
                for ch in self.dir_map.get(node, [])
            ]
        )
        self.nodes[node] = 2
        return has_cycle

    def solve(self, A, B):
        self.nodes = [0] * A
        self.dir_map = {}
        for u, v in B:
            self.dir_map.setdefault(u - 1, set())
            self.dir_map[u - 1].add(v - 1)

        return int(any([self.nodes[i] == 0 and self.dfs(i) for i in range(A)]))
