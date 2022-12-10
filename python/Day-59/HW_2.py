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
    def get_count(self, A):
        if not A:
            return 0

        if A.val < self.B:
            return self.get_count(A.right)
        elif A.val > self.C:
            return self.get_count(A.left)

        return 1 + self.get_count(A.right) + self.get_count(A.left)

    def solve(self, A, B, C):
        self.B = B
        self.C = C

        return self.get_count(A)
