import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        dist = [-1]*A

        adj_map = {i:set() for i in range(A)}

        for st, end, wt in B:
            adj_map[st].add((wt, end))
            adj_map[end].add((wt, st))
        
        X = [(0, C)]
        vis = set()
        heapq.heapify(X)

        while(X):
            cur_dist, node = heapq.heappop(X)
            vis.add(node)
            if dist[node] == -1 or dist[node] > cur_dist:
                dist[node] = cur_dist
            
            for c_d, c_n in adj_map[node]:
                if c_n not in vis:
                    heapq.heappush(X, (c_d+cur_dist, c_n))

        return dist
