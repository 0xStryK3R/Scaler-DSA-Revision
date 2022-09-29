class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        hash_points = {}
        N = len(A)
        for i in range(N):
            hash_points.setdefault(A[i], set())
            hash_points[A[i]].add(B[i])

        ans = 0
        for i in range(N):
            for j in range(i + 1, N):
                if (
                    A[i] != A[j]
                    and B[i] != B[j]
                    and B[j] in hash_points[A[i]]
                    and B[i] in hash_points[A[j]]
                ):
                    ans += 1

        return ans // 2
