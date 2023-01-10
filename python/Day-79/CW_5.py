class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        set_0 = set(range(1, A+1))
        indegree = {}
        adj_mat = {i+1:set() for i in range(A)}
        
        for u, v in B:
            if v not in adj_mat[u]:
                adj_mat[u].add(v)
                set_0.discard(v)
                indegree[v] = indegree.get(v, 0) + 1
        
        ans = []
        while(set_0):
            min_node = min(set_0)
            set_0.discard(min_node)
            ans.append(min_node)
            for child in adj_mat[min_node]:
                indegree[child] -= 1
                if not indegree[child]:
                    set_0.add(child)
        return ans