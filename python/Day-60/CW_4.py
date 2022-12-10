# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        if not A:
            return None
        A.right = self.flatten(A.right)

        if A.left:
            left_LL_head = self.flatten(A.left)
            A.left = None
            left_LL_tail = left_LL_head

            while left_LL_tail.right:
                left_LL_tail = left_LL_tail.right

            left_LL_tail.right = A.right

            A.right = left_LL_head

        return A
