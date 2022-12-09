# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        headl = taill = headr = tailr = None
        while A:
            if A.val < B:
                if not headl:
                    headl = taill = A
                else:
                    taill.next = A
                    taill = taill.next
            else:
                if not headr:
                    headr = tailr = A
                else:
                    tailr.next = A
                    tailr = tailr.next
            A = A.next

        if not (headl and headr):
            return headl or headr

        if tailr:
            tailr.next = None
        if taill:
            taill.next = headr

        return headl
