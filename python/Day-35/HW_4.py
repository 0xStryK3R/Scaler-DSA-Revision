class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(32):
            bit_pos = 0
            for num in A:
                bit_pos += (num & (1 << i)) >> i
            ans += bit_pos % 3 << i
        return ans
