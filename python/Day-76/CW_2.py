MOD = 10**9 + 7
class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
    def max_val(self, root):
        if self.dp[root] == -1:
            with_children = sum([self.max_val(child) for child in self.c.get(root, [])])
            without_children = self.B[root - 1] + sum([self.max_val(gg_child) for gg_child in self.ggc.get(root, [])])
            self.dp[root] = max(with_children, without_children)
            
        return self.dp[root]

    def solve(self, A, B):
        N = len(A)

        self.c = {}
        self.ggc = {}
        for i, par in enumerate(A[1:]):
            self.c[par] = self.c.get(par, []) + [i+2]
            if par!=1:
                gp = A[par-1]
                if gp!=1:
                    ggp = A[gp-1]
                    self.ggc[ggp] = self.ggc.get(ggp, []) + [i+2]
                    
        self.B = B
        self.dp = [-1]*(N+1)
        
        self.max_val(1)

        return self.dp[1]%MOD