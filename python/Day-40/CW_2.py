class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A = sorted(list(set(A)))

        N = len(A)
        if N < 2:
            return 0 if B != 0 else 1

        pair_count = 0

        l = 0
        r = 1

        while r < N:
            if A[r] - A[l] > B:
                l += 1
            elif A[r] - A[l] < B:
                r += 1
            else:
                pair_count += 1
                l += 1
                r += 1
            if l == r:
                r += 1
        return pair_count
