def get_pf():
    n = 10**6 + 1
    primes = [-1] * n
    p = 2

    while p < n:
        if primes[p] < 0:
            primes[p] = p
            for i in range(p * p, n, p):
                if primes[i] < 0:
                    primes[i] = p
        p += 1

    return primes


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        primes = get_pf()

        lpf_cnt_map = {}

        for lpf in primes:
            lpf_cnt_map[lpf] = lpf_cnt_map.get(lpf, 0) + 1

        return [lpf_cnt_map[i] for i in B]
