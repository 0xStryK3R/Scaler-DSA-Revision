class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        N = len(A)
        stack = []
        r_max = []
        for i in range(N - 1, -1, -1):
            while stack and stack[-1] <= A[i]:
                stack.pop()

            if stack:
                r_max.append(stack[-1])
            else:
                r_max.append(-1)
            stack.append(A[i])

        r_max = r_max[::-1]

        return r_max
