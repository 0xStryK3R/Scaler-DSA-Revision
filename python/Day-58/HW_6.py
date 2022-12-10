# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if not A:
            return 0

        if A.left and A.right:
            return min(self.minDepth(A.left), self.minDepth(A.right)) + 1
        else:
            return (self.minDepth(A.left) or self.minDepth(A.right)) + 1
