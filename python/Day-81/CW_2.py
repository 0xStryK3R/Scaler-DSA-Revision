class Solution:
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
                    answer[i] = 1

            for u, v, i in wt_map[w]:
                self.union(u, v)

        return answer
