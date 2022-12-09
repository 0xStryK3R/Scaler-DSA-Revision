# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        top_up = 0
        C = ListNode(0)

        new_list = C

        while A and B:
            next_val = A.val + B.val + top_up
            top_up = next_val // 10
            next_val %= 10
            A = A.next
            B = B.next
            C.next = ListNode(next_val)
            C = C.next

        A = A or B

        while A:
            next_val = A.val + top_up
            top_up = next_val // 10
            next_val %= 10
            A = A.next
            C.next = ListNode(next_val)
            C = C.next

        if top_up:
            C.next = ListNode(top_up)

        return new_list.next
