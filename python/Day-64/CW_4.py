def get_max_child_idx(A, cur_idx):
    N = len(A)
    max_child = lc = (cur_idx<<1)+1
    rc = lc + 1
    if rc<N and A[rc]>A[lc]:
        max_child = rc
    return max_child

def heapify(A, cur_idx):
    N = len(A)
    max_child = get_max_child_idx(A, cur_idx)
    while(max_child<N and A[cur_idx]<A[max_child]):
        A[cur_idx], A[max_child] = A[max_child], A[cur_idx] 
        cur_idx = max_child
        max_child = get_max_child_idx(A, cur_idx)
    return

def create_max_heap(A):
    #heapify logic
    N = len(A)
    for cur_idx in range((N>>1)-1, -1, -1):
        heapify(A, cur_idx)
    return A

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        B = create_max_heap(B)
        ans = 0
        for i in range(A):
            ans += B[0]
            B[0] = B[0]>>1
            heapify(B, 0)
        
        return ans%(10**9+7)
        
