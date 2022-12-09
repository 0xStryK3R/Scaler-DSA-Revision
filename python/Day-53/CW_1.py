# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        head = A

        for i in range(B):
            head = head.next
            if not head:
                return A.next

        sec = A
        while head.next:
            head = head.next
            sec = sec.next

        sec.next = sec.next.next

        return A
