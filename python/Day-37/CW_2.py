class Solution:
    # @param A : string
    # @return a strings
    def getGoodBase(self, digit_size, A):
        l = 2
        r = A - 2

        while(l<=r):
            m = (l+r)>>1
            digit_sum = 0
            for i in range(digit_size):
                digit_sum += m**i
                if digit_sum>A:
                    break
            if digit_sum > A:
                r = m - 1
            elif digit_sum < A:
                l = m + 1
            else:
                return m
        
        return A

    def solve(self, A):
        A = int(A)
        ans = min([self.getGoodBase(i, A) for i in range(2, 61)]+[A-1])
        return str(ans)
