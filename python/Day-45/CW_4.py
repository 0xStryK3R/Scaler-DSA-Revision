class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        B = A + "$" + B + B[:-1]
        N = len(B)
        Z = [0] * N
        Z[0] = N
        L = R = 0
        ans = 0

        for i in range(1, N):
            if i > R:
                L = R = i
                while R < N and B[R] == B[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
            else:
                j = i - L
                if Z[j] < R - i + 1:
                    Z[i] = Z[j]
                else:
                    L = i
                    while R < N and B[R] == B[R - L]:
                        R += 1
                    Z[i] = R - L
                    R -= 1
            if Z[i] == len(A):
                ans += 1
        return ans
