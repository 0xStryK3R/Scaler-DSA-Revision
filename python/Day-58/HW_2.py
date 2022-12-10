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
        nxt_level = [A]
        ans = []
        while nxt_level:
            cur_row = []
            cur_level = nxt_level
            nxt_level = []
            for next_node in cur_level:
                cur_row.append(next_node.val)
                if next_node.left:
                    nxt_level.append(next_node.left)
                if next_node.right:
                    nxt_level.append(next_node.right)
            ans.append(cur_row[-1])
        return ans
