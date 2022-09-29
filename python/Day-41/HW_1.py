class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        sumA = minA = maxA = A[0]
        for i in range(1, N):
            num = A[i]
            sumA += num
            minA = min(minA, num)
            maxA = max(maxA, num)

        if sumA == N * (maxA + minA) // 2:
            return 1
        else:
            return 0
