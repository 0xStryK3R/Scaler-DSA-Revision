class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        N = len(A)
        i = 0
        while i < N:
            while 0 < A[i] <= N and A[i] != i + 1 and A[i] != A[A[i] - 1]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
            i += 1

        for i in range(N):
            if A[i] != i + 1:
                return i + 1

        return N + 1
