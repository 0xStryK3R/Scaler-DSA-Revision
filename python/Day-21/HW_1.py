class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        return list(map(sum, zip(*A)))
