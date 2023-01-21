class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        dsu = [i for i in range(n + 1)]

        def find(x):
            while x != dsu[x]:
                dsu[x] = dsu[dsu[x]]
            return dsu[x]

        ans = 0
        for i in range(1, n):
            u = i + 1
            v = A[i]
            if v == 1:
                one = 1
            dsu[find(u)] = find(v)
        for i in range(1, n + 1):
            if dsu[i] == i:
                ans += 1
        return ans - 1
