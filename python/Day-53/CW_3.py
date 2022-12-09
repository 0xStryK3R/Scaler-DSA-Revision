# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None
def mid_LL(A, even_mid_left=False):
    slow = fast = A
    if even_mid_left:
        fast = fast.next
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    
    return slow
    
def rev_LL(A):
    new_LL = None
    while(A):
        next_node = A
        A = A.next
        next_node.next = new_LL
        new_LL = next_node
    return new_LL
    
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def reorderList(self, A):
        pre_mid_element = mid_LL(A, True)
        right_half_rev = rev_LL(pre_mid_element.next)
        
        pre_mid_element.next = None
        left_half = A
        
        finall_LL = left_half
        
        while(right_half_rev):
            new_node = right_half_rev
            right_half_rev = right_half_rev.next
            
            new_node.next = left_half.next
            left_half.next = new_node
            left_half = left_half.next.next
        
        return finall_LL
	    
