import sys

sys.setrecursionlimit = 10**6


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A < 2:
            return 1

        a = b = c = 1
        mod = 10003

        for i in range(2, A + 1):
            c = (b + (i - 1) * a) % mod
            a = b
            b = c

        return c % mod
