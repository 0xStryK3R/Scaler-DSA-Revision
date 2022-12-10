# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer

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

    def postorderTraversal(self, A):
        stack = []
        ans = []

        while A or stack:
            if A:
                ans.append(A.val)
                stack.append(A)
                A = A.right
            else:
                A = stack.pop()
                A = A.left

        return ans[::-1]

    def solve(self, A, B, C):
        inorder_map = {val: i for i, val in enumerate(B)}
        try:
            return int(
                C
                == self.postorderTraversal(
                    self.create_tree(A, inorder_map, 0, len(A) - 1, 0, len(A) - 1)
                )
            )
        except:
            return 0
