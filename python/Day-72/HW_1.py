import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param s : string
    # @param p : string
    # @return an integer
    def match(self, i, j):
        if i < 0 and j < 0:
            return True

        if j < 0:
            return False

        if i < 0:
            return j == 1 and self.p[j] == "*"

        if self.dp[i][j] == -1:
            if self.p[j] in (".", self.s[i]):
                self.dp[i][j] = self.match(i - 1, j - 1)
            elif self.p[j] == "*":
                self.dp[i][j] = self.match(i, j - 2)
                if self.p[j - 1] in (self.s[i], "."):
                    self.dp[i][j] |= self.match(i - 1, j)
            else:
                self.dp[i][j] = False

        return self.dp[i][j]

    def isMatch(self, s, p):
        self.s = s
        self.p = p
        N = len(s)
        M = len(p)

        self.dp = [[-1] * M for _ in range(N)]

        return int(self.match(N - 1, M - 1))
