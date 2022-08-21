class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        N, M = len(A), len(A[0])
        l = 0
        r = N * M - 1

        while l <= r:
            mid = (l + r) >> 1
            x, y = mid // M, mid % M

            if A[x][y] > B:
                r = mid - 1
            elif A[x][y] < B:
                l = mid + 1
            else:
                return 1

        return 0
