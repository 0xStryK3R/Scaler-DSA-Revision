class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        num = den = 1
        for i in range(2, A + 1):
            num *= A + i
            den *= i

        return num // den
