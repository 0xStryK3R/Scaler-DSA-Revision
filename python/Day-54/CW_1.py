# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None
def mid_LL(A, even_mid_left=True):
    slow = fast = A
    if even_mid_left:
        fast = fast.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def rev_LL(A):
    new_LL = None
    while A:
        next_node = A
        A = A.next
        next_node.next = new_LL
        new_LL = next_node
    return new_LL


class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        mid_node = mid_LL(A).next
        rev_mid_node = rev_LL(mid_node)

        while rev_mid_node:
            if A.val == rev_mid_node.val:
                A = A.next
                rev_mid_node = rev_mid_node.next
            else:
                return 0
        return 1
