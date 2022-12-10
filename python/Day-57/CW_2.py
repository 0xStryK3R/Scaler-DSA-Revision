# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if not A:
            return None
        root_val = B.pop()
        root = TreeNode(root_val)

        root_pos = A.index(root_val)

        root.left = self.buildTree(A[:root_pos], B[:root_pos])
        root.right = self.buildTree(A[root_pos + 1 :], B[root_pos:])

        return root
