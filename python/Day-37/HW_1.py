class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def is_max_allocation(self, m, PS_arr, B, N):
        next_valid_page_num = PS_arr[-1]
        remaining_students = B

        for i in range(N - 1, -1, -1):

            if PS_arr[i - 1] < next_valid_page_num:
                next_valid_page_num = PS_arr[i] - m
                remaining_students -= 1

            if next_valid_page_num <= 0:
                return True

            elif not remaining_students:
                return False

        return True

    def paint(self, B, C, A):
        mod = 10000003
        N = len(A)

        if B == 1:
            return sum(A) * C % mod
        elif N < B:
            return max(A) * C % mod

        PS_arr = [0] * N
        PS_arr[0] = max_max_allocation = A[0]

        for i in range(1, N):
            PS_arr[i] = PS_arr[i - 1] + A[i]
            if i == N - B:
                max_max_allocation = PS_arr[i]
            if i > N - B:
                max_max_allocation = max(
                    max_max_allocation, PS_arr[i] - PS_arr[i - (N - B + 1)]
                )

        l = min_max_allocation = max(max(A), PS_arr[-1] // B)
        r = max_max_allocation

        while r > l:
            m = (l + r) // 2
            if self.is_max_allocation(m, PS_arr, B, N):
                r = m
            else:
                l = m + 1

        return r * C % mod
