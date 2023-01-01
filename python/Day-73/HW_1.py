class Solution:
    # @param A : list of list of integers
    # @return an integer
    def largets_histogram_area(self, A):
        N = len(A)

        stack = []
        l_min = []
        for i in range(N):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()

            if stack:
                l_min.append(stack[-1])
            else:
                l_min.append(-1)
            stack.append(i)

        stack = []
        r_min = []
        for i in range(N - 1, -1, -1):
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()

            if stack:
                r_min.append(stack[-1])
            else:
                r_min.append(N)
            stack.append(i)
        r_min = r_min[::-1]

        ans = 0

        for i in range(N):
            ans = max(ans, A[i] * (r_min[i] - l_min[i] - 1))

        return ans

    def maximalRectangle(self, A):
        for r in range(1, len(A)):
            for c in range(len(A[0])):
                if A[r][c] == 1:
                    A[r][c] += A[r - 1][c]

        ans = 0
        for row in A:
            ans = max(ans, self.largets_histogram_area(row))

        return ans
