class Solution:
    # @param A : tuple of integers
    # @return a strings
    def fractional_value(self, n):
        if n == 0:
            return 0
        x = n
        denom = 1
        while x:
            x //= 10
            denom *= 10
        denom -= 1
        return n / denom

    def largestNumber(self, A):
        A = list(A)
        A.sort(key=self.fractional_value, reverse=True)

        return str(int("".join(list(map(str, A)))))
