# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : list of integers
    # @return a list of list of integers
    def floor(self, root, x):
        if not root:
            return -1
        
        if root.val>x:
            return self.floor(root.left, x)
        
        if root.val==x:
            return x
        
        return max(root.val, self.floor(root.right, x))
        
    def ceil(self, root, x):
        if not root:
            return float('inf')
        
        if root.val<x:
            return self.ceil(root.right, x)
        
        if root.val==x:
            return x
        
        return min(root.val, self.ceil(root.left, x))

    def solve(self, A, B):
        ans = []

        for num in B:
            f = self.floor(A, num)
            c = self.ceil(A, num)
            if c == float('inf'):
                c = -1
            ans.append([f, c])

        return ans