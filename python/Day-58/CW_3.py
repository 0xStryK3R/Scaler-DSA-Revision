# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def height(self, root):
        if not root:
            return 0

        left_ht = self.height(root.left)
        right_ht = self.height(root.right)

        self.diameter = max(self.diameter, left_ht + right_ht + 1)

        return max(left_ht, right_ht) + 1

    def solve(self, A):
        self.diameter = 0
        self.height(A)

        return self.diameter - 1
