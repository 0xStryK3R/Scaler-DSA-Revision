class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        mod = 1000000007
        N = [0 for x in range(len(A))]
        A = [int(i) for i in A]
        if A[0] > 0:
            N[0] = 1
        for i in range(1, len(A)):
            if A[i] > 0:
                N[i] += N[i-1]
                N[i] %= mod
            if 10 <= A[i-1]*10 + A[i] <= 26:
                if i == 1:
                    N[i] += 1
                    N[i] %= mod
                else:
                    N[i] += N[i-2]
                    N[i] %= mod
        return N[-1] % mod
