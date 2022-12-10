# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def check_symmetry(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        return (
            root1.val == root2.val
            and self.check_symmetry(root1.left, root2.right)
            and self.check_symmetry(root1.right, root2.left)
        )

    def isSymmetric(self, A):
        return int(self.check_symmetry(A.left, A.right))
