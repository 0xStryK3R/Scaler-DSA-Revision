class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        freq_map_A = {}

        for num in A:
            freq_map_A[num] = freq_map_A.get(num, 0) + 1

        ans = []

        for num in B + sorted(freq_map_A):
            ans += [num] * freq_map_A.pop(num, 0)

        return ans
