class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = A[0]
        for i in A[1:]:
            ans = ans ^ i
        return ans
