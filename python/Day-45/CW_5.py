class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)
        Z = [0] * N
        Z[0] = N
        L = R = 0

        for i in range(1, N):
            if i > R:
                # Outside Window - Brute Force
                L = R = i
                while R < N and A[R] == A[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
            else:
                # Inside Window
                j = i - L
                if Z[j] < R - i + 1:
                    # Before Boundary - Copy Paste
                    Z[i] = Z[j]
                else:
                    # Touching/Outside Boundary - Brute Force
                    L = i
                    while R < N and A[R] == A[R - L]:
                        R += 1
                    Z[i] = R - L
                    R -= 1
            # Factor check not done as main string can have substring of repeating pattern at the end.
            if Z[i] + i == N:
                return i
        return N
