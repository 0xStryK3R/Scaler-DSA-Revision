def merge(l1, l2):
    dummy = ListNode(0)
    head = dummy

    while (l1 and l2):
        # find the smaller node
        if (l1.val <= l2.val):
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    # add the remaining nodes
    head.next = l1 if l1 else l2
    return dummy.next


def sortL(head):
    if (head == None or head.next == None): 
        return head
    pre, fast, slow = head, head, head
    
    # find the middle node
    while (fast and fast.next):
        pre = slow
        slow = slow.next
        fast = fast.next.next

    pre.next = None
    return merge(sortL(head), sortL(slow))
    

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
	    return sortL(A)
