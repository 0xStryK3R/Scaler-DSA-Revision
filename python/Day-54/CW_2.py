# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
def pal_len(fwd_ll, rev_ll):
    cnt = 0
    while(fwd_ll and rev_ll):
        if fwd_ll.val != rev_ll.val:
            break
        cnt += 2
        fwd_ll = fwd_ll.next
        rev_ll = rev_ll.next
    
    return cnt

class Solution:
    # @param A : head node of linked list
    # @return an integer
        
    def solve(self, A):
        max_pal = 0
        head = A
        rev_head = None
        
        while(head):
            cur_node = head
            head = head.next
            
            max_pal = max(max_pal, pal_len(head, rev_head) + 1)
            
            cur_node.next = rev_head
            rev_head = cur_node
            
            max_pal = max(max_pal, pal_len(head, rev_head))
            
        return max_pal