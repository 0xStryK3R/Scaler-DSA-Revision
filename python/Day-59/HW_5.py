# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack = []

        ans = []

        while A or stack:
            if A:
                stack.append(A)
                A = A.left
            else:
                A = stack.pop()
                ans.append(A.val)
                A = A.right

        return ans

    def solve(self, A, B):
        iot1 = self.inorderTraversal(A)
        iot2 = self.inorderTraversal(B)

        i = j = 0
        output = []

        while i < len(iot1) and j < len(iot2):
            if iot1[i] < iot2[j]:
                output.append(iot1[i])
                i += 1
            else:
                output.append(iot2[j])
                j += 1

        if i < len(iot1):
            output.extend(iot1[i:])
        if j < len(iot2):
            output.extend(iot2[j:])

        return output
