# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        ans_head = new_chain = ListNode(0)

        while A and A.next:
            first, second = A, A.next
            A = A.next.next
            new_chain.next = second
            second.next = first
            first.next = None
            new_chain = new_chain.next.next

        if A:
            new_chain.next = A

        return ans_head.next
