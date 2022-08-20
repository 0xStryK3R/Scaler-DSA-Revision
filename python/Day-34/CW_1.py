m = 1000003


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        N = len(A)
        freq_map = {}
        for ch in A:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        uniq_ch = list(freq_map.keys())
        uniq_ch.sort()

        numerator = fact(N)

        denominator = 1
        for freq in freq_map.values():
            denominator *= fact(freq)

        final_rank = 1
        for i in range(N):
            numerator //= N - i
            offset_numerator = 0
            j = 0
            while uniq_ch[j] != A[i]:
                offset_numerator += freq_map[uniq_ch[j]]
                j += 1
            if offset_numerator:
                final_rank += (numerator * offset_numerator) // denominator
            denominator //= freq_map[A[i]]
            freq_map[A[i]] -= 1

        return final_rank % m
