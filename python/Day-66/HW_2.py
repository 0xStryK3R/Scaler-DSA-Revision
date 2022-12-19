class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        bit_count = 10
        coins = 0

        while bit_count > -1:
            pow5 = 5**bit_count
            if A >= pow5:
                coins += A // pow5
                A %= pow5
            bit_count -= 1

        return coins
