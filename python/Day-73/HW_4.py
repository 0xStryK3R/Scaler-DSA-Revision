def lenLongestFibSubseq(A):
    N = len(A)
    index = {}
    for i in range(N):
        index[A[i]] = i
    longest = {}
    ans = 0
    for k in range(N):
        for j in range(k):
            if A[k] - A[j] < A[j] and index.get(A[k] - A[j]) != None:
                i = index[A[k] - A[j]]
                if longest.get(i * N + j) == None:
                    longest[i * N + j] = 0
                longest[j * N + k] = longest[i * N + j] + 1
                ans = max(ans, longest[j * N + k] + 2)
    if ans >= 3:
        return ans
    return 0

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        return lenLongestFibSubseq(A)
