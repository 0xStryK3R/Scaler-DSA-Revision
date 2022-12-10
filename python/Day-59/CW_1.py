# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A, i=0, j=None):
        if j == None:
            j = len(A) - 1

        if i == j:
            return TreeNode(A[i])

        if j < i:
            return None

        mid = (i + j) >> 1
        root = TreeNode(A[mid])

        root.left = self.sortedArrayToBST(A, i, mid - 1)
        root.right = self.sortedArrayToBST(A, mid + 1, j)

        return root
