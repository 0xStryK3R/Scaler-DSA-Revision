class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A = list(A)
        for swap_count in range(B):
            mini = swap_count
            for i, v in enumerate(A[swap_count:]):
                if v < A[mini]:
                    mini = i + swap_count
            A[mini], A[swap_count] = A[swap_count], A[mini]
        return A[swap_count]
