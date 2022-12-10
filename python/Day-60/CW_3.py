# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
import sys

sys.setrecursionlimit(10**6)


def tree_sum(A):
    if not A:
        return 0

    left_sum = tree_sum(A.left)
    right_sum = tree_sum(A.right)

    A.sum = left_sum + right_sum + A.val
    return A.sum


def check_partition(A, total_tree_sum):
    if not A:
        return 0

    if (A.left and A.left.sum == total_tree_sum - A.left.sum) or (
        A.right and A.right.sum == total_tree_sum - A.right.sum
    ):
        return 1

    return check_partition(A.left, total_tree_sum) or check_partition(
        A.right, total_tree_sum
    )


class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        tree_sum(A)
        return check_partition(A, A.sum)
