import heapq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj_map = {i: set() for i in range(1, A + 1)}

        for u, v, w in B:
            adj_map[u].add((w, v))
            adj_map[v].add((w, u))

        st = 1
        vis = set([st])
        edge_heap = list(adj_map[st])

        heapq.heapify(edge_heap)
        answer = 0

        while len(vis) < A:
            w, u = heapq.heappop(edge_heap)
            if u in vis:
                continue
            answer += w
            vis.add(u)

            for c_w, v in adj_map[u]:
                heapq.heappush(edge_heap, (c_w, v))

        return answer % (10**9 + 7)
