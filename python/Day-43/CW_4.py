class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        hash_set = set(A)
        max_length = 1
        for num in hash_set:
            if num - 1 in hash_set:
                continue
            start = num
            while num + 1 in hash_set:
                num += 1
                max_length = max(max_length, num - start + 1)
        return max_length
