class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer
    def make_tree(self, root):
        self.tree_mat[root] = set()
        for ch in self.adj_mat[root]:
            if ch not in self.tree_mat:
                self.tree_mat[root].add(ch)
                self.make_tree(ch)
                
    def maxmin(self, root):
        cur_val = self.A[root-1]
        maxi = mini = cur_val
        for ch in self.tree_mat[root]:
            mini, *_, maxi = sorted([*self.maxmin(ch), maxi, mini])
        
        self.max_diff = max(self.max_diff, abs(cur_val-maxi), abs(cur_val-mini))
        return maxi, mini

    def solve(self, A, B):
        self.adj_mat = {i+1:set() for i, _ in enumerate(A)}
        self.A = A
        for u, v in B:
            self.adj_mat[u].add(v)
            self.adj_mat[v].add(u)
        
        self.tree_mat = {}
        self.make_tree(1)
        
        self.max_diff = 0
        self.maxmin(1)
        return self.max_diff