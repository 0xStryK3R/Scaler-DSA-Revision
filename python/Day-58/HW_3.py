# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def vot(self, A, idx=0, lvl=0):
        if not A:
            return

        self.ans_dict.setdefault(idx, {})
        self.ans_dict[idx].setdefault(lvl, [])
        self.ans_dict[idx][lvl].append(A.val)
        self.vot(A.left, idx - 1, lvl + 1)
        self.vot(A.right, idx + 1, lvl + 1)

    def solve(self, A):
        self.ans_dict = {}
        self.vot(A)

        ans = []

        for key in sorted(self.ans_dict.keys()):
            row = []
            ans.extend(self.ans_dict[key][min(self.ans_dict[key].keys())])

        return ans
