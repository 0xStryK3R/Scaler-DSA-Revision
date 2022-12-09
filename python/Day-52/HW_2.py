class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        aux_queue = []
        for i in range(B):
            aux_queue.append(A[i])
        
        top = 0
        while(top<B):
            A[B-top-1] = aux_queue[top]
            top += 1

        return A
