class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)

        stack = []
        l_max = []
        for i in range(N):
            while stack and A[stack[-1]] < A[i]:
                stack.pop()

            if stack:
                l_max.append(stack[-1])
            else:
                l_max.append(-1)
            stack.append(i)

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
        r_max = []
        for i in range(N - 1, -1, -1):
            while stack and A[stack[-1]] < A[i]:
                stack.pop()

            if stack:
                r_max.append(stack[-1])
            else:
                r_max.append(N)
            stack.append(i)
        r_max = r_max[::-1]

        stack = []
        r_min = []
        for i in range(N - 1, -1, -1):
            while stack and A[stack[-1]] > A[i]:
                stack.pop()

            if stack:
                r_min.append(stack[-1])
            else:
                r_min.append(N)
            stack.append(i)
        r_min = r_min[::-1]

        ans = 0
        for i in range(N):
            num = A[i]
            l_max_range = i - l_max[i]
            l_min_range = i - l_min[i]
            r_max_range = r_max[i] - i
            r_min_range = r_min[i] - i

            ans += num * (l_max_range * r_max_range - l_min_range * r_min_range)

        return ans % (10**9 + 7)
