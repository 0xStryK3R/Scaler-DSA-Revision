class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        prefix = A.pop()

        for word in A:
            min_len = min(len(prefix), len(word))
            prefix = prefix[:min_len]
            word = word[:min_len]
            for i in range(min_len):
                if word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break

        return prefix
