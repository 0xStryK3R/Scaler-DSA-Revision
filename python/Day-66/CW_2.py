class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        N = len(A)
        x_arr = []
        for i in range(N):
            if A[i] == "x":
                x_arr.append(i)

        if not x_arr:
            return 0

        N = len(x_arr)
        median_idx = x_arr[(N - 1) // 2]
        lt_cnt = (N - 1) // 2
        rt_cnt = N - (N - 1) // 2 - 1

        total_displacement = 0

        for idx in x_arr:
            total_displacement += abs(idx - median_idx)

        total_displacement -= lt_cnt * (lt_cnt + 1) // 2
        total_displacement -= rt_cnt * (rt_cnt + 1) // 2

        return total_displacement % (10**7 + 3)
