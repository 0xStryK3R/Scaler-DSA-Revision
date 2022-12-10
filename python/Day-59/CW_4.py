# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def check(self, root, lower=float("-inf"), upper=float("inf")):
        if root is None:
            return True

        return (
            lower < root.val < upper
            and self.check(root.left, lower, root.val)
            and self.check(root.right, root.val, upper)
        )

    def isValidBST(self, A):
        return int(self.check(A))
