# Definition for a  binary tree node
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        if not A:
            return 0

        stack = []

        tmp_set = set()

        while A or stack:
            if A:
                stack.append(A)
                A = A.left
            else:
                A = stack.pop()
                num = A.val
                if B - num in tmp_set:
                    return 1
                tmp_set.add(num)
                A = A.right

        return 0
