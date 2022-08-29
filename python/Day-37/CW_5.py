class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def check_sum(self, A, B, m):
        # checks if all m-sized subarray sum <B
        sum_subarr = 0
        for i in range(len(A)):
            sum_subarr += A[i]
            if i >= m:
                sum_subarr -= A[i - m]

            if sum_subarr > B:
                return False

        return True

    def solve(self, A, B):
        l = 1
        r = len(A)
        ans = -1

        while l <= r:
            m = (l + r) >> 1
            if self.check_sum(A, B, m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans
