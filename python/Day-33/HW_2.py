class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        zero_cnt = 0

        while A:
            zero_cnt += A // 5
            A //= 5

        return zero_cnt
