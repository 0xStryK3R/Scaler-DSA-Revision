class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        cum_xor = 0

        xor_map_freq = {}
        xor_map_sum = {}

        xor_count = 0

        for i, num in enumerate(A):
            xor_map_freq[cum_xor] = xor_map_freq.get(cum_xor, 0) + 1
            xor_map_sum[cum_xor] = xor_map_sum.get(cum_xor, 0) + i

            cum_xor ^= num

            if cum_xor in xor_map_freq:
                xor_count += i * xor_map_freq[cum_xor] - xor_map_sum[cum_xor]
        return xor_count % (10**9 + 7)
