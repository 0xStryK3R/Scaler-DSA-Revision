class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)

        l = 0
        r = N - 1

        while l < r:
            mid = (l + r) >> 1
            if mid & 1:
                if A[mid] != A[mid - 1]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if A[mid] != A[mid + 1]:
                    r = mid
                else:
                    l = mid + 2

        return A[l] if l == r else A[mid]
