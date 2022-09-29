class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        A.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return A[:B]
