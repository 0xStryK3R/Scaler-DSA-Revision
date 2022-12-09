def removeLoop(loop_node, head):
    ptr1 = loop_node
    ptr2 = loop_node
    k = 1
    while ptr1.next != ptr2:
        ptr1 = ptr1.next
        k += 1
    ptr1 = head
    ptr2 = head
    for i in range(k):
        ptr2 = ptr2.next
    while ptr2 != ptr1:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    while ptr2.next != ptr1:
        ptr2 = ptr2.next
    ptr2.next = None
    return head


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        slow_p = A
        fast_p = A
        ans = None
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            # If slow_p and fast_p meet at some point then there is a loop
            if slow_p == fast_p:
                if slow_p.next == fast_p:
                    slow_p.next = None
                    return A
                ans = removeLoop(slow_p, A)
                return ans
