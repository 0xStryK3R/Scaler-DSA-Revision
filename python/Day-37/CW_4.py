class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def gcd(self, A, B):
        B,A = sorted([abs(A),abs(B)])
        if B==0:
            return A
        return self.gcd(B, A%B)
      
    def solve(self, A, B, C):
        mod = 10**9 + 7
        hcf = B*C//self.gcd(B, C)
        
        l = min(B, C)
        r = 2**64
        
        while(l<=r):
            m = (l+r)>>1
            k = m//B + m//C - m//hcf
            
            if k<A:
                l = m + 1
            elif k>A:
                r = m - 1
            else:
                break

        n = max((m//B)*B, (m//C)*C)

        return n%mod
        
        
        
