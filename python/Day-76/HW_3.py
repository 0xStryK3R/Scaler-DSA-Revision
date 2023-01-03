def kadane(A):
    ans = -1000000000000
    n = len(A)
    sm = 0
    for i in range(n):
        if(sm + A[i] > 0):
            sm += A[i]
        else:
            sm = 0
        ans = max(ans, sm)
    return ans


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        ans = -10000000000
        n = len(A)
        m = len(A[0])
        for left in range(m):
            temp = [0] * n
            for right in range(left, m):
                for k in range(n):
                    temp[k] += A[k][right]
                ans = max(kadane(temp), ans)

        return ans
