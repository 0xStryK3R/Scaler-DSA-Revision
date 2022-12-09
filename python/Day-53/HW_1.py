# Definition for singly-linked list.
# class ListNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        if B == C:
            return A
        ans = main_tail = ListNode(0)
        rev_tail = main_tail.next = A

        i = 1

        while A:
            if i > C:
                break
            if i < B:
                main_tail = main_tail.next
                rev_tail = rev_tail.next
                A = A.next
            else:
                tmp = A.next
                A.next = main_tail.next
                main_tail.next = A
                A = tmp
            i += 1

        rev_tail.next = A
        return ans.next
