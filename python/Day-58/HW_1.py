# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys

sys.setrecursionlimit(10**6)
from collections import deque


class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A, i=0):
        root = TreeNode(A[0])
        q = deque()
        q.append(root)
        i = 1
        while len(q) != 0:
            cur = q.popleft()
            if cur == None:
                continue
            val_left = A[i]
            val_right = A[i + 1]
            i += 2
            if val_left == -1:
                cur.left = None
            else:
                cur.left = TreeNode(val_left)
            if val_right == -1:
                cur.right = None
            else:
                cur.right = TreeNode(val_right)
            q.append(cur.left)
            q.append(cur.right)
        return root
