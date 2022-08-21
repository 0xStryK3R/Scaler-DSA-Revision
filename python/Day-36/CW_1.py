class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)

        l = 0
        r = N - 1

        while l <= r:
            mid = (l + r) >> 1

            if mid < N - 1 and A[mid] < A[mid + 1]:
                l = mid + 1
            elif mid > 0 and A[mid] < A[mid - 1]:
                r = mid - 1
            else:
                break
        return A[mid]
