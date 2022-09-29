class Solution:
    # @param A : integer
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        char_freq_map = {}
        for char in B:
            char_freq_map.setdefault(char, 0)
            char_freq_map[char] += 1

        for char, freq in char_freq_map.items():
            if freq % A != 0:
                return -1

        return 1
