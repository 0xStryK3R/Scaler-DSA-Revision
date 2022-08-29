class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def isvalidDistance(self, d, A, B):
        prev = A[0]
        B -= 1
        for stall in A[1:]:
            if stall - prev >= d:
                prev = stall
                B -= 1
        
        if B<1:
            return True

        return False


    def solve(self, A, B):
        A.sort()
        N = len(A)

        prev = A[0]

        largest_dist = (A[-1] - A[0])//(B-1)
        smallest_dist = largest_dist

        for stall in A[1:]:
            smallest_dist = min(smallest_dist, stall - prev)
            prev = stall
        
        l = smallest_dist
        r = largest_dist

        while(l+1<r):
            m = (l+r)>>1

            if self.isvalidDistance(m, A, B):
                l = m
            else:
                r = m - 1

        return r if self.isvalidDistance(r, A, B) else l