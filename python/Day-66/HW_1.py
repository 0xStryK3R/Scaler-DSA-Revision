class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A = list(map(int, list(A)))
        n = len(A)
        temp = [0] * n

        xr = 0
        ans = 0
        i = 0
        while(i <= n - B):
            xr ^= temp[i]
            if A[i]==xr:
                ans += 1
                if(i + B < n):
                    temp[i+B] = 1
                xr ^= 1
            i += 1

        while(i < n):
            xr ^= temp[i]
            if(A[i] ^ xr == 0):
                return -1
            i += 1

        return ans