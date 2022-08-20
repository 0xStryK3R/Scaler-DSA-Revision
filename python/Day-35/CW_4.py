class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        N = len(A)

        if N < 3:
            return A

        for bit_pos in range(32):
            bit_0 = 0
            bit_1 = 0
            for num in A:
                if num & (1 << bit_pos):
                    bit_1 = bit_1 ^ num
                else:
                    bit_0 = bit_0 ^ num

            if bit_0 + bit_1 != 0:
                return sorted([bit_0, bit_1])
