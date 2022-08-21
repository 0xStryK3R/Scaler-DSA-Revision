class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        N = len(A)
        l = 0
        r = N - 1

        while l + 1 < r:
            mid = (l + r) >> 1

            if A[mid] < A[-1]:
                r = mid
            else:
                l = mid

        if A[l] > A[r]:
            if B <= A[-1]:
                l, r = r, N - 1
            else:
                l, r = 0, l
        else:
            l, r = 0, N - 1

        while l <= r:
            m = (l + r) >> 1
            if A[m] == B:
                return m
            elif A[m] > B:
                r = m - 1
            else:
                l = m + 1

        return -1
