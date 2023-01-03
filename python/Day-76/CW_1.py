# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return an integer
    def max_path_sum(self, root):
        if not root:
            return 0
        
        ls = max(0, self.max_path_sum(root.left))
        rs = max(0, self.max_path_sum(root.right))

        self.max_path = max(self.max_path, root.val + ls + rs)

        return root.val + max(ls, rs)

	def maxPathSum(self, A):
        self.max_path = A.val
        self.max_path_sum(A)

        return self.max_path
