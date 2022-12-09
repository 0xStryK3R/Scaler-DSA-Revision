class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        count = 0

        while B:
            nxt = B.pop(0)
            while A[0] != nxt:
                A.append(A.pop(0))
                count += 1
            A.pop(0)
            count += 1

        return count
