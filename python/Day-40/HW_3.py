class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def get_diff(self, A, B, C, i, j, k):
        return max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

    def minimize(self, A, B, C):
        i = j = k = 0
        M = len(A)
        N = len(B)
        R = len(C)
        max_diff = self.get_diff(A, B, C, i, j, k)

        while max_diff and i < M and j < N and k < R:
            max_diff = min(max_diff, self.get_diff(A, B, C, i, j, k))
            if i < M - 1 and A[i] < B[j] and A[i] < C[k]:
                i += 1
            elif j < N - 1 and B[j] < C[k]:
                j += 1
            elif k < R - 1:
                k += 1
            else:
                break
        return max_diff
