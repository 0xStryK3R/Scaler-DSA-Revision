# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []

        ans = []

        while A or stack:
            if A:
                stack.append(A)
                A = A.left
            else:
                A = stack.pop()
                ans.append(A.val)
                A = A.right

        return ans
