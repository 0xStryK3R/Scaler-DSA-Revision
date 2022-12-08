def z_algo(A):
    N = len(A)
    Z = [0] * N
    Z[0] = N
    L = R = 0

    for i in range(1, N):
        if i > R:
            L = R = i
            while R < N and A[R] == A[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            j = i - L
            if Z[j] < R - i + 1:
                Z[i] = Z[j]
            else:
                L = i
                while R < N and A[R] == A[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        N = len(A)
        A = A + "$" + A[::-1]
        ans = N - max(z_algo(A)[N + 1 :])

        return ans
