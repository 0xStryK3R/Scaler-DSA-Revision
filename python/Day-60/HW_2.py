# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if not A:
            return int(not B)

        rem = B - A.val

        lt = self.hasPathSum(A.left, rem)
        rt = self.hasPathSum(A.right, rem)

        if not A.right:
            return lt

        if not A.left:
            return rt

        return lt or rt
