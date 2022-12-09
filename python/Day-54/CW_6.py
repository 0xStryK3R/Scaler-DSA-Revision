class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


def clonelist(A):
    tmp_LL = A
    while tmp_LL:
        new_node = ListNode(tmp_LL.val)
        new_node.next = tmp_LL.next
        tmp_LL.next = new_node
        tmp_LL = new_node.next
    tmp_LL = A

    while tmp_LL:
        tmp_LL.next.random = tmp_LL.random.next
        tmp_LL = tmp_LL.next.next

    tmp_LL = A.next
    new_LL = tmp_LL

    while tmp_LL.next:
        tmp_LL.next = tmp_LL.next.next
        tmp_LL = tmp_LL.next

    return new_LL
