class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def create_tree(self, A, inorder_map, pre_st, pre_end, in_st, in_end):
        if pre_st > pre_end or pre_st >= len(A) or in_st > in_end or in_st >= len(A):
            return None

        root = TreeNode(A[pre_st])
        root_idx = inorder_map[A[pre_st]]

        root.left = self.create_tree(
            A, inorder_map, pre_st + 1, pre_st + root_idx - in_st, in_st, root_idx - 1
        )
        root.right = self.create_tree(
            A, inorder_map, pre_st + root_idx - in_st + 1, pre_end, root_idx + 1, in_end
        )

        return root

    def leaf_traversal(self, root):
        if not root:
            return

        if not root.left and not root.right:
            self.leaves.append(root.val)
        else:
            self.leaf_traversal(root.left)
            self.leaf_traversal(root.right)

    def solve(self, A):
        inorder_map = {val: i for i, val in enumerate(sorted(A))}
        bst = self.create_tree(A, inorder_map, 0, len(A) - 1, 0, len(A) - 1)
        self.leaves = []
        self.leaf_traversal(bst)

        return self.leaves
