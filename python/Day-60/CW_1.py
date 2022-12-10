# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def find_lca(self, A, B, C):
        if not A:
            return False, False

        b_in_left, c_in_left = self.find_lca(A.left, B, C)
        b_in_right, c_in_right = self.find_lca(A.right, B, C)

        b_found = b_in_left or b_in_right or A.val == B
        c_found = c_in_left or c_in_right or A.val == C

        if b_found and c_found:
            self.ans = A.val
            b_found, c_found = False, False

        return b_found, c_found

    def lca(self, A, B, C):
        self.ans = -1
        self.find_lca(A, B, C)

        return self.ans
