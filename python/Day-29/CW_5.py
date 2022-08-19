class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        N = len(A)
        lt_max_arr = [0]
        rt_max_arr = [0]

        for i in range(N):
            lt_max_arr.append(max(lt_max_arr[-1], A[i]))

        for i in range(N - 1, -1, -1):
            rt_max_arr.append(max(rt_max_arr[-1], A[i]))

        rt_max_arr = rt_max_arr[::-1]

        cap = 0
        for i in range(N):
            adj_ht = min(lt_max_arr[i], rt_max_arr[i + 1])
            if adj_ht > A[i]:
                cap += adj_ht - A[i]

        return cap
