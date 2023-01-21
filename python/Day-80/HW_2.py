import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : list of integers
    # @return an integer
    def get_ht(self, root):
        self.vis.add(root)
        child_hts = [0, 0]
        for child in self.adj_map[root]:
            if child in self.vis:
                continue
            child_hts.append(self.get_ht(child))

        max_child = max(child_hts)
        child_hts.remove(max_child)

        self.max_dist = max(self.max_dist, max_child + 1 + max(child_hts))

        return max_child + 1

    def solve(self, A):
        N = len(A)
        adj_map = {i: set() for i in range(N)}

        for u, v in enumerate(A):
            if v == -1:
                root = u
                continue

            adj_map[u].add(v)
            adj_map[v].add(u)

        self.max_dist = 0
        self.vis = set()
        self.adj_map = adj_map

        self.get_ht(root)

        return self.max_dist - 1
