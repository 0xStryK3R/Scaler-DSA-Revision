class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        N = len(A)
        if N < 3:
            return A[0]

        freq_map = {}

        for num in A:
            freq_map[num] = freq_map.get(num, 0) + 1
            while len(freq_map.keys()) == 3:
                dict_keys = list(freq_map.keys())
                for k in dict_keys:
                    freq_map[k] -= 1
                    if not freq_map[k]:
                        freq_map.pop(k)

        for candidate in freq_map.keys():
            if A.count(candidate) > N // 3:
                return candidate

        return -1
