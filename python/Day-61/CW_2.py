# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

INF = float("inf")


class Solution:
    # @param A : root node of tree
    # @return an integer
    def check_bst(self, root):
        # print(root.val)
        if not root.left and not root.right:
            return True, root.val, 1, root.val

        if root.left:
            lbst, lmin, lsz, lmax = self.check_bst(root.left)
            # print(root.val, self.max_bst_size, lbst, lmin, lsz, lmax)
            if not root.right:
                if lbst and lmax < root.val:
                    self.max_bst_size = max(self.max_bst_size, lsz + 1)
                return (lbst and lmax < root.val), lmin, lsz + 1, root.val

        if root.right:
            rbst, rmin, rsz, rmax = self.check_bst(root.right)
            # print(root.val, self.max_bst_size, rbst, rmin, rsz, rmax)
            if not root.left:
                if rbst and root.val < rmin:
                    self.max_bst_size = max(self.max_bst_size, rsz + 1)
                return (rbst and root.val < rmin), root.val, rsz + 1, rmax

        if lbst and rbst and lmax < root.val < rmin:
            self.max_bst_size = max(self.max_bst_size, lsz + rsz + 1)
        return (lbst and rbst and lmax < root.val < rmin), lmin, lsz + rsz + 1, rmax

    def solve(self, A):
        if not A:
            return 0

        self.max_bst_size = 1

        self.check_bst(A)

        return self.max_bst_size
