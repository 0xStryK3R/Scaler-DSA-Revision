# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def left_boundary_traversal(self, root):
        if not root:
            return

        self.left_trav.append(root.val)
        if root.left:
            self.left_boundary_traversal(root.left)
        elif root.right:
            self.left_boundary_traversal(root.right)

    def right_boundary_traversal(self, root):
        if not root:
            return

        if root.right:
            self.right_boundary_traversal(root.right)
        elif root.left:
            self.right_boundary_traversal(root.left)
        self.right_trav.append(root.val)

    def leaf_traversal(self, root):
        if not root:
            return

        if not root.left and not root.right:
            self.leaves.append(root.val)
        else:
            self.leaf_traversal(root.left)
            self.leaf_traversal(root.right)

    def solve(self, A):
        if not A:
            return []

        self.left_trav = []
        self.left_boundary_traversal(A)

        self.right_trav = []
        self.right_boundary_traversal(A)

        self.leaves = []
        self.leaf_traversal(A)

        return self.left_trav[:-1] + self.leaves[:-1] + self.right_trav[:-1]
