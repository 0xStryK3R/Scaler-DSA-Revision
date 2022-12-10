# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if not A:
            return 0

        if B <= A.val <= C:
            return self.solve(A.left, B, C) + self.solve(A.right, B, C) + 1
        else:
            if A.val > C:
                return self.solve(A.left, B, C)
            else:
                return self.solve(A.right, B, C)
