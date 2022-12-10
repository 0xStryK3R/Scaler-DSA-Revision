# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
mod = 1000000007


def inOrder(A, a):
    if A == None:
        return
    inOrder(A.left, a)
    a.append(A.val)
    inOrder(A.right, a)


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def solve(self, A, B):
        a = []
        b = []
        inOrder(A, a)
        inOrder(B, b)
        i = 0
        j = 0
        n = len(a)
        m = len(b)
        ans = 0
        while i < n and j < m:
            if a[i] < b[j]:
                i += 1
            elif b[j] < a[i]:
                j += 1
            else:
                ans += a[i]
                ans %= mod
                i += 1
                j += 1
        return ans
