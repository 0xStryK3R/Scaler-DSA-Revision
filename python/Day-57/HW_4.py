# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):
        if not root:
            return None

        inverted_left = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = inverted_left

        return root
