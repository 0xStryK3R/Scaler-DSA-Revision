# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):

        if len(A) == 1:
            return A[0]

        l = 0
        r = len(A)
        mid = (l + r) // 2

        # Divide the problem into two parts, solve for them separately and merge both the sorted lists.
        l = self.mergeKLists(A[:mid])
        r = self.mergeKLists(A[mid:])

        return self.merge(l, r)

    def merge(self, l, r):
        dummy = ListNode(0)

        itr = dummy
        while l and r:
            if l.val < r.val:
                itr.next = l
                l = l.next
            else:
                itr.next = r
                r = r.next

            itr = itr.next

        if l:
            itr.next = l
        else:
            itr.next = r

        return dummy.next
