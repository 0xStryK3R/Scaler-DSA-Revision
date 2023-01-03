from math import log, ceil
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def get_ht(self, root):
        children = [0, 0]
        
        for child in self.adj_mat.get(root, []):
            if child not in self.vis_set:
                self.vis_set.add(child)
                child_ht = self.get_ht(child)
                children.append(child_ht)
        
        children.sort()
        max1 = children.pop()
        max2 = children.pop()

        self.diameter = max(self.diameter, max1 + max2 + 1)
        
        return max1 + 1
    
    
    def get_dia(self, A, B):
        no_src = set(range(1, A+1))
        self.vis_set = set()
        self.adj_mat = {}
        for u, v in B:
            self.adj_mat.setdefault(u, set())
            self.adj_mat[u].add(v)
            self.adj_mat.setdefault(v, set())
            self.adj_mat[v].add(u)
            no_src.discard(v)
        
        root = no_src.pop()
        self.vis_set.add(root)
        self.get_ht(root)
    
    def solve(self, A, B):
        self.diameter = 0
        self.get_dia(A, B)
        
        if self.diameter<3:
            ans = 0
        else:
            ans = ceil(log(self.diameter - 1, 2))
        return ans