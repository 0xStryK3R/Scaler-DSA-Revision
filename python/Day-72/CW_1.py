class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):

        # num_ways[i] will be storing the number of solutions for
        # sum i. We need N+1 rows as the table is constructed
        # in bottom up manner using the base case (N = 0)
        num_ways = [0] * (B + 1)
        m = len(A)
        MOD = 1000007
        # Base case (If required sum is 0)
        num_ways[0] = 1

        # Pick all coins one by one and update the num_ways[] values
        for i in range(0, m):
            for j in range(A[i], B + 1):
                num_ways[j] += num_ways[j - A[i]]
                num_ways[j] %= MOD
        return num_ways[B]
