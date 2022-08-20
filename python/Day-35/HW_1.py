class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        if B == -1:
            return -A

        bit_pos = 0
        ans = 0
        sign = 1
        if A ^ B < 0:
            sign = -1
        A = abs(A)
        B = abs(B)

        while A >= B:
            if A >= B << bit_pos:
                bit_pos += 1
            else:
                bit_pos -= 1
                ans += 1 << bit_pos
                A -= B << bit_pos
                bit_pos = 0

        return ans * sign
