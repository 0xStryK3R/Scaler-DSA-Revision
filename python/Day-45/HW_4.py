class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def smallestPrefix(self, A, B):
        N = len(A)
        ans = A[0]
        B = B[0]
        ord_B = ord(B)
        for i in range(1, N):
            if ord(A[i]) >= ord_B:
                break
            ans += A[i]

        return ans + B
