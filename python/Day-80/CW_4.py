class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        N = len(A)
        inf = float("inf")
        for i in range(N):
            for j in range(N):
                if A[i][j]==-1:
                    A[i][j] = inf

        for k in range(N):
            for u in range(N):
                for v in range(N):
                    A[u][v] = min(A[u][v], A[u][k] + A[k][v])
                    
        for i in range(N):
            for j in range(N):
                if A[i][j]==inf:
                    A[i][j] = -1
        return A