# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def recoverTree(self, A):
		prev = None
		rt_stck = []
		ans = []
		while(A or rt_stck):
			if A:
				rt_stck.append(A)
				A = A.left
			else:
				A = rt_stck.pop()
				if prev and A.val<prev:
					if ans:
						ans[0] = A.val
					else:
						ans = [A.val, prev]
				prev = A.val
				A = A.right
		return ans