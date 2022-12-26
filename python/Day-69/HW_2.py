class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        n = len(A)
        # store the result that is the max we have found so far
        r = A[0]
        # imax/imin stores the max/min product of
        # subarray that ends with the current number A[i]
        imax = r
        imin = r
        for i in range(1, n):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if A[i] < 0:
                imax, imin = imin, imax

            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            imax = max(A[i], imax * A[i])
            imin = min(A[i], imin * A[i])

            # the newly computed max value is a candidate for our global result
            r = max(r, imax)
        return r
