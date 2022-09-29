class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = list(set(A))
        max_1 = max_2 = A[0]
        for num in A:
            if num > max_1:
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_2 = num

        return max_2 % max_1
