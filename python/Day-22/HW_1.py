class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        ans = A[1] - A[0]

        for i in range(1, len(A)):
            ans = min(ans, A[i] - A[i - 1])

        return ans
