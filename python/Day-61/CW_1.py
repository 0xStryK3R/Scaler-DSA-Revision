# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
def child_sum_tree(root):
    if not root:
        return 0

    child_sum = child_sum_tree(root.left) + child_sum_tree(root.right)
    root.val = max(root.val, child_sum)

    return root.val


def re_distribute(root):
    if not root or not (root.left or root.right):
        return

    diff = root.val
    if root.left:
        diff -= root.left.val

    if root.right:
        diff -= root.right.val

    if diff > 0:
        if root.left:
            root.left.val += diff
        else:
            root.right.val += diff

    re_distribute(root.left)
    re_distribute(root.right)
    return


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        child_sum_tree(A)
        re_distribute(A)
        return A
