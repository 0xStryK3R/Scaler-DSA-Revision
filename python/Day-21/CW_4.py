class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        min_sum = sumk = sum(A[:B])
        ans = 0

        i = B
        while(i<len(A)):
            sumk += (-A[i-B] + A[i])
            if sumk<min_sum:
                ans = i - B + 1
                min_sum = sumk
            i += 1
        
        return ans

        
