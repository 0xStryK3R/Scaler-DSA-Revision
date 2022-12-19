class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()

        return max(list(map(lambda x: abs(x[0] - x[1]), zip(A, B))))
