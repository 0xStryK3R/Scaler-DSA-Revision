class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @param G : list of integers
    # @param H : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F, G, H):
        inf = float("inf")
        adj_mat = [[inf] * A for _ in range(A)]

        for i in range(A):
            adj_mat[i][i] = 0

        for u, v, w in zip(D, E, F):
            u -= 1
            v -= 1
            adj_mat[u][v] = min(adj_mat[u][v], w)
            adj_mat[v][u] = min(adj_mat[v][u], w)

        for k in range(A):
            for u in range(A):
                for v in range(A):
                    adj_mat[u][v] = min(adj_mat[u][v], adj_mat[u][k] + adj_mat[k][v])

        answer = []

        for u, v in zip(G, H):
            tmp = adj_mat[u - 1][v - 1]
            if tmp == inf:
                tmp = -1
            answer.append(tmp)

        return answer
