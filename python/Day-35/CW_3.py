class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        m = 10**9 + 7
        N = len(A)
        ans = 0
        for i in range(32):
            count = 0
            for num in A:
                count += (num >> i) & 1
            ans = (ans + (count * (N - count)) % m) % m

        return (ans * 2) % m


# References: https://www.geeksforgeeks.org/sum-of-bit-differences-among-all-pairs/
