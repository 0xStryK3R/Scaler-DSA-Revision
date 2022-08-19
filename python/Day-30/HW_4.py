class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == B:
                    return (i + 1) * 1009 + j + 1
        return -1
