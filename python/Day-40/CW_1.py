class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq_map = {}
        pair_count = 0

        for i in A:
            pair_count += freq_map.get(B - i, 0)
            freq_map[i] = freq_map.get(i, 0) + 1

        return pair_count % (10**9 + 7)
