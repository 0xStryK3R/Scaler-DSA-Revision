class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def pow(self, A, B, mod):
        if B == 0:
            return 1
        y = self.pow(A, B // 2, mod)
        if B & 1:
            return (((A * y) % mod) * y) % mod
        else:
            return (y * y) % mod

    def solve(self, A, B):
        A %= B
        return self.pow(A, B - 2, B)
