class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        N = len(A)
        ps_arr = [0]
        for num in A:
            ps_arr.append(ps_arr[-1] + num)

        ps_arr = ps_arr[1:]

        lt_min_ps = [0]

        for num in ps_arr:
            lt_min_ps.append(min(lt_min_ps[-1], num))

        lt_min_ps = lt_min_ps[:-1]

        rt_max_ps = [ps_arr[-1]]
        for num in ps_arr[::-1]:
            rt_max_ps.append(max(rt_max_ps[-1], num))

        rt_max_ps = rt_max_ps[::-1][:-1]

        return max(list(map(lambda x: x[1] - x[0], zip(lt_min_ps, rt_max_ps))))
