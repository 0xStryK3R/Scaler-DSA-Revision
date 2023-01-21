class KruskalsAlgo:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
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

    def solve(self, A, B):
        max_wt = 0
        self.P = list(range(A))

        N = len(B)
        answer = [0] * N

        wt_map = {}

        for i, data in enumerate(B):
            u, v, w = data
            wt_map.setdefault(w, set())
            wt_map[w].add((u - 1, v - 1, i))

        for w in sorted(wt_map.keys()):
            for u, v, i in wt_map[w]:
                x = self.find(u)
                y = self.find(v)
                if x != y:
                    max_wt = max(max_wt, w)
            for u, v, i in wt_map[w]:
                self.union(u, v)

        return max_wt


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def get_ref(self, i, j):
        return i * self.B + j

    def solve(self, A, B, C):
        self.B = B
        dir_map = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        edge_list = []

        for i in range(A):
            for j in range(B):
                for dx, dy in dir_map:
                    if -1 < i + dx < A and -1 < j + dy < B:
                        u = self.get_ref(i, j)
                        v = self.get_ref(i + dx, j + dy)
                        edge_list.append([u, v, abs(C[i][j] - C[i + dx][j + dy])])

        edge_list.sort()
        max_wt = KruskalsAlgo().solve(A * B, edge_list)

        return max_wt
