def get_pf_cnt(A):
    pf_cnt = [0] * (A + 1)
    pf_cnt[1] = 0
    p = 2

    while p <= A:
        if not pf_cnt[p]:
            for i in range(p, A + 1, p):
                pf_cnt[i] += 1
        p += 1

    return pf_cnt


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        pf_cnt = get_pf_cnt(A)

        return len(list(filter(lambda x: x == 2, pf_cnt)))
