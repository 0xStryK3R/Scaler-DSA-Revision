# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        C = ListNode(0)
        new_merged_list = C

        while A and B:
            if A.val < B.val:
                C.next = A
                A = A.next
            else:
                C.next = B
                B = B.next
            C = C.next
            C.next = None

        C.next = A or B

        return new_merged_list.next
