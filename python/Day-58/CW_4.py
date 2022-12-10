# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        if not A:
            return 0

        height = 0
        queue = [A]

        while queue:
            height += 1
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            queue = next_level

        return height
