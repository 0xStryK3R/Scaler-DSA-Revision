class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mod = 10**9 + 7

        cnt_dict = {}
        for i in A:
            cnt_dict.setdefault(i, 0)
            cnt_dict[i] += 1

        ans = 0

        for i, i_cnt in cnt_dict.items():
            for j, j_cnt in cnt_dict.items():
                ans = ans + i_cnt * j_cnt * (i % j)
                ans = ans % mod

        return ans
