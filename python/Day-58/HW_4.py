# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        queue = [A]
        lot = []

        while queue:
            next_level = []
            cur_level = []
            for node in queue:
                cur_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            queue = next_level
            if len(lot) & 1:
                lot.append(cur_level[::-1])
            else:
                lot.append(cur_level)

        return lot
