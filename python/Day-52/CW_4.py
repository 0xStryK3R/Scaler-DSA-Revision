from collections import deque

# https://www.geeksforgeeks.org/deque-in-python/


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        max_arr = []
        de = deque()

        N = len(A)

        if B >= N:
            return [max(A)]

        for i in range(B):
            while de and A[de[-1]] < A[i]:
                de.pop()
            de.append(i)

        max_arr.append(A[de[0]])

        for i in range(B, N):
            if i - de[0] >= B:
                de.popleft()
            while de and A[de[-1]] < A[i]:
                de.pop()
            de.append(i)
            max_arr.append(A[de[0]])

        return max_arr
