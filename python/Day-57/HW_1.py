# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(A, inorder_map, pre_st, pre_end, in_st, in_end):
    if pre_st > pre_end or pre_st >= len(A) or in_st > in_end or in_st >= len(A):
        return None

    root = TreeNode(A[pre_st])
    root_idx = inorder_map[A[pre_st]]

    root.left = create_tree(
        A, inorder_map, pre_st + 1, pre_st + root_idx - in_st, in_st, root_idx - 1
    )
    root.right = create_tree(
        A, inorder_map, pre_st + root_idx - in_st + 1, pre_end, root_idx + 1, in_end
    )

    return root


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        inorder_map = {val: i for i, val in enumerate(B)}
        return create_tree(A, inorder_map, 0, len(A) - 1, 0, len(A) - 1)
