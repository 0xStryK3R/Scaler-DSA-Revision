# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def check(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        ls = self.check(root.left)
        rs = self.check(root.right)

        if ls + rs != root.val:
            self.check_sum_bt = 0

        return ls + rs + root.val

    def solve(self, A):
        if not A:
            return 1

        self.check_sum_bt = 1
        self.check(A)

        return self.check_sum_bt
