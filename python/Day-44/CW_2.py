class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def gcd(self, A, B):
        while B:
            A, B = B, A % B
        return A

    def solve(self, A, B):
        N = len(A)
        ans = 0
        for i in range(N):
            slope_map = {}
            offset = 1
            max_freq = 0
            for j in range(i + 1, N):
                X = A[j] - A[i]
                Y = B[j] - B[i]
                if X == Y == 0:
                    offset += 1
                else:
                    gcdXY = self.gcd(X, Y)
                    X //= gcdXY
                    Y //= gcdXY
                    if Y < 0:
                        Y *= -1
                        X *= -1

                    slope_map.setdefault((X, Y), 0)
                    slope_map[(X, Y)] += 1

                    max_freq = max(max_freq, slope_map[(X, Y)])
            ans = max(ans, max_freq + offset)
        return ans
