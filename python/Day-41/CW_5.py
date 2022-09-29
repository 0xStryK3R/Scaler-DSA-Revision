class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        B = sorted(A)
        if A == B:
            return [-1]

        N = len(A)
        i = 0

        while i < N:
            if A[i] != B[i]:
                break
            i += 1

        j = N - 1
        while j > -1:
            if A[j] != B[j]:
                break
            j -= 1

        return [i, j]
