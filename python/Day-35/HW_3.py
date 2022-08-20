class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        bit_pos = 0

        # For smaller number (B), flip just the existing bits in A
        while A >> bit_pos:
            ans += ((A >> bit_pos) & 1 ^ 1) << bit_pos
            bit_pos += 1

        # The larger number (C), will just be next higher power of 2
        # Also, simply adding will suffice, since B and C will not have
        # the same set bits.
        ans += 1 << bit_pos
        return ans
