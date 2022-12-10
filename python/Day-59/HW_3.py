# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.root = root
        self.stack = []

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.root or self.stack

    # @return an integer, the next smallest number
    def next(self):
        if self.root:
            self.stack.append(self.root)
            self.root = self.root.left
            ans = self.next()
        else:
            self.root = self.stack.pop()
            ans = self.root.val
            self.root = self.root.right
        return ans


# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),
