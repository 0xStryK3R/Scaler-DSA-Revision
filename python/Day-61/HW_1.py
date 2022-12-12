# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers

    def get_paths(self, A, B):
        if not A:
            return
        B.append(A.val)

        if not A.left and not A.right:
            self.ans.append(B.copy())
            B.pop()
            return

        if A.left:
            self.get_paths(A.left, B)
        if A.right:
            self.get_paths(A.right, B)

        B.pop()

    def solve(self, A):
        if not A:
            return []

        self.ans = []
        self.get_paths(A, [])

        return self.ans
