class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        l, r = 0, len(A) - 1

        while r - l > 1:
            m = (l + r) // 2
            if A[m] == B:
                return m
            if A[m] > B:
                r = m - 1
            else:
                l = m

        if B <= A[l]:
            return 0
        elif B > A[r]:
            return r + 1
        else:
            return r
