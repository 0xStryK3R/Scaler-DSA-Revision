class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        mod = 10**9 + 7
        min_q = []
        max_q = []
        min_top = -1
        max_top = -1

        ans = 0

        for i, num in enumerate(A):
            if not min_q:
                min_q.append(i)
                min_top += 1
            else:
                if min_q[min_top] <= (i - B):
                    min_top += 1
                while min_q and A[min_q[-1]] > num:
                    min_q.pop()
                min_q.append(i)
                if min_top > len(min_q) - 1:
                    min_top = len(min_q) - 1

            if not max_q:
                max_q.append(i)
                max_top += 1
            else:
                if max_q[max_top] <= (i - B):
                    max_top += 1
                while max_q and A[max_q[-1]] < num:
                    max_q.pop()
                max_q.append(i)
                if max_top > len(max_q) - 1:
                    max_top = len(max_q) - 1

            if i >= B - 1:
                ans += A[min_q[min_top]] + A[max_q[max_top]]

        return ans % mod
