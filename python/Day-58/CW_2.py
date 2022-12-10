# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        ans = []
        queue = [A]

        while queue:
            next_level = []
            for node in queue:
                if node:
                    ans.append(node.val)
                else:
                    ans.append(-1)
                    continue
                next_level.append(node.left)
                next_level.append(node.right)
            queue = next_level

        return ans
