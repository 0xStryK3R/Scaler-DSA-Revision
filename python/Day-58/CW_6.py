# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        height = 0
        queue = [A]
        left_view = []

        while queue:
            height += 1
            next_level = []
            cur_level = []
            for node in queue:
                cur_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            queue = next_level
            left_view.append(cur_level[0])

        return left_view
