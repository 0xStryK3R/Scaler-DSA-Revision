# Solution Reference: https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/


def upper_bound_bs(num, lis):
    l = 0
    n = len(lis)
    ans = r = n - 1
    while l <= r:
        m = (l + r) // 2
        if lis[m] == num:
            return m
        elif lis[m] > num:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans


class Solution:
    # @param A : list of integers
    # @return an integer
    def lis(self, A):
        lis = [A[0]]

        for num in A[1:]:
            if num < lis[0]:
                lis[0] = num
            elif num > lis[-1]:
                lis.append(num)
            else:
                upper_bound_idx = upper_bound_bs(num, lis)
                lis[upper_bound_idx] = num

        return len(lis)
