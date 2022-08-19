class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = []
        N, M = len(A), len(B)

        i = j = 0

        while i < N and j < M:
            if A[i] < B[j]:
                ans.append(A[i])
                i += 1
            else:
                ans.append(B[j])
                j += 1

        ans.extend(A[i:])
        ans.extend(B[j:])

        return ans
