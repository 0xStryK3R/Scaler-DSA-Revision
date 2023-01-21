class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        if C==D:
            return 0
        adj_mat = {i:set() for i in range(A)}
        
        for st, end, wt in B:
            wt -= 1
            while(wt):
                adj_mat[st].add(A)
                adj_mat[A] = set([st])
                st = A
                A += 1
                wt -= 1
            adj_mat[st].add(end)
            adj_mat[end].add(st)

        bfs_queue = [C]
        vis_set = set(bfs_queue)
        ans = []
        
        while(bfs_queue):
            ans.append(bfs_queue)
            cur_lvl = bfs_queue
            bfs_queue = []
            for i in cur_lvl:
                vis_set.add(i)
                unvis_children = adj_mat[i]-vis_set
                bfs_queue.extend(unvis_children)
            if D in bfs_queue:
                return len(ans)
            
        return -1
