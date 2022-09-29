class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        dict_A = {}
        ans = 0
        N = len(A)
        start_index = 0
        for i in range(N):
            if A[i] in dict_A:
                ans = max(ans, i - start_index)
                start_index = max(dict_A[A[i]] + 1, start_index)
            dict_A[A[i]] = i

        ans = max(ans, N - start_index)
        return ans
