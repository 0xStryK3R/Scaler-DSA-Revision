# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers

    def get_paths(self, A, B, arr):
        if not A:
            return

        B -= A.val
        arr.append(A.val)

        if not A.left and not A.right:
            if not B:
                self.ans.append(arr.copy())
            arr.pop()
            return

        if A.left:
            self.get_paths(A.left, B, arr)
        if A.right:
            self.get_paths(A.right, B, arr)

        arr.pop()

    def pathSum(self, A, B):
        if not A:
            return []

        self.ans = []
        self.get_paths(A, B, [])

        return self.ans
