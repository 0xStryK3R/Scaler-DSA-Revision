# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        reord_ll = None
        prev_tail = cur_tail = None

        while A:
            cur_tail = A
            rev_seg = None
            for i in range(B):
                cur_node = A
                A = A.next
                cur_node.next = rev_seg
                rev_seg = cur_node

            if reord_ll:
                prev_tail.next = rev_seg
            else:
                reord_ll = rev_seg

            prev_tail = cur_tail

        return reord_ll
