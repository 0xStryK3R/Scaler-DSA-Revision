class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        N = len(A)
        if N < 2:
            return 0

        for s in range(N - 1):
            if A[s] > A[s + 1]:
                break

        if s == N - 2:
            return 0

        for e in range(N - 1, 0, -1):
            if A[e] < A[e - 1]:
                break

        min_se = min(A[s : e + 1])
        max_se = max(A[s : e + 1])

        for i in range(s):
            if A[i] > min_se:
                s = i
                break

        for i in range(N - 1, e, -1):
            if A[i] < max_se:
                e = i
                break

        return e - s + 1
