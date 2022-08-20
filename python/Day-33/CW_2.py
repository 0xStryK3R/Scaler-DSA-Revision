class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def pow(self, A, B, mod):
        if B==0:
            return 1
        y = self.pow(A, B//2, mod)
        if B&1:
            return (((A*y)%mod)*y)%mod
        else:
            return (y*y)%mod
            
    def solve(self, A, B):
        p = 10**9 + 7
        A %= p
        r = 1
        for i in range(1, B+1):
            r = (r*i)%(p-1)

        ans = self.pow(A,r,p)
        return ans
        