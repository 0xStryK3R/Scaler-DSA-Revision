# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        cur_level = [root]
        while cur_level:
            next_level = []
            cur_node = cur_level[0]
            if cur_node.left:
                next_level.append(cur_node.left)
            if cur_node.right:
                next_level.append(cur_node.right)
            for next_node in cur_level[1:]:
                cur_node.next = next_node
                cur_node = next_node
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)
            cur_level = next_level

        return root
