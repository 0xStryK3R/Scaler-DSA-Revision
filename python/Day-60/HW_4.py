# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

sys.setrecursionlimit(10**6)


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        stack = []

        head = prev = TreeNode(0)

        while A or stack:
            if A:
                stack.append(A)
                A = A.left
            else:
                A = stack.pop()
                prev.right = A
                A.left = prev
                prev = A
                A = A.right

        prev.right = head.right
        head = head.right
        if head:
            head.left = prev

        return head
