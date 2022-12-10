# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

INF = float("inf")


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def find_lca(self, A, B, C):
        if not A:
            return False, INF, False, INF

        b_in_left, b_left_dist, c_in_left, c_left_dist = self.find_lca(A.left, B, C)
        b_in_right, b_right_dist, c_in_right, c_right_dist = self.find_lca(
            A.right, B, C
        )

        b_found = b_in_left or b_in_right or A.val == B
        if A.val == B:
            b_dist = 0
        else:
            b_dist = min(b_left_dist, b_right_dist) + 1

        c_found = c_in_left or c_in_right or A.val == C
        if A.val == C:
            c_dist = 0
        else:
            c_dist = min(c_left_dist, c_right_dist) + 1

        if b_found and c_found:
            self.ans = A.val
            self.dist = b_dist + c_dist
            b_found, c_found = False, False

        return b_found, b_dist, c_found, c_dist

    def solve(self, A, B, C):
        self.ans = -1
        self.dist = None
        self.find_lca(A, B, C)

        return self.dist
