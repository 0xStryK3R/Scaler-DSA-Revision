class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        N = len(A)

        dec_suffix = N
        i = N - 1

        while i > 0:
            if A[i] > A[i - 1]:
                dec_suffix = i
                break
            i -= 1

        if dec_suffix == N:
            return A[::-1]

        A = A[:dec_suffix] + A[dec_suffix:][::-1]
        for j in range(dec_suffix, N):
            if A[dec_suffix - 1] < A[j]:
                A[j], A[dec_suffix - 1] = A[dec_suffix - 1], A[j]
                break

        return A
