class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        count_a = 0
        N = len(A)
        for i in range(N):
            if A[i] == "a":
                count_a += 1
        return count_a * (count_a + 1) // 2
