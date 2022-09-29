class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        l = 0
        r = len(A) - 1

        max_cap = min(A[l], A[r]) * (r - l)

        while l < r:
            max_cap = max(max_cap, min(A[l], A[r]) * (r - l))

            if A[l] < A[r]:
                l += 1
            else:
                r -= 1

        return max_cap
