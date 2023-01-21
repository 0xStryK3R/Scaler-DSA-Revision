def get_adj(A):
    N = len(A)
    M = len(A[0])
    adj_mat = [[set() for j in range(M)] for i in range(N)]
    st_row = [0]*M
    for i in range(N):
        st_pt = 0
        for j in range(M):
            if A[i][j] == 1:
                st_pt = j+1
                st_row[j] = i+1
            else:
                if st_pt != j:
                    adj_mat[i][j].add(((i, st_pt), j-st_pt))
                if st_row[j] != i:
                    adj_mat[i][j].add(((st_row[j], j), i - st_row[j]))
                    
    st_row = [N-1]*M
    for i in range(N-1, -1, -1):
        st_pt = M - 1
        for j in range(M-1, -1, -1):
            if A[i][j] == 1:
                st_pt = j-1
                st_row[j] = i-1
            else:
                if st_pt != j:
                    adj_mat[i][j].add(((i, st_pt), st_pt-j))
                if st_row[j]  != i:
                    adj_mat[i][j].add(((st_row[j], j), st_row[j]-i))
            
    return adj_mat

class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        if B==C:
            return 0
        if A[B[0]][B[1]]==1 or A[C[0]][C[1]]==1:
            return -1
        adj_mat = get_adj(A)
        B = tuple(B)
        C = tuple(C)
        
        #BFS Part
        bfs_queue = [(B, 0)]
        vis_set = set(B)

        while(bfs_queue):
            next_level = []
            for p, rd in bfs_queue:
                vis_set.add(p)
                for ch, d in adj_mat[p[0]][p[1]]:
                    if ch==C:
                        return  rd+d
                        
                    if ch not in vis_set:
                        next_level.append((ch, rd+d))
            bfs_queue = next_level
                
        return -1