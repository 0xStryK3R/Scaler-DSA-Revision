class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        freq_map = {}
        for num in A:
            freq_map[num] = freq_map.get(num, 0) + 1

        cnt = 0
        freq_arr = list(freq_map.values())
        freq_arr.sort()

        for num in sorted(freq_map.keys()):
            freq = freq_map[num]
            if freq > 1:
                freq -= 1
                cnt += freq
                i = num + 1
                while freq and i not in freq_map:
                    freq -= 1
                    cnt += freq
                    i += 1
                if freq:
                    freq_map[i] += freq
                    freq = 0
                    cnt += freq

        return cnt
