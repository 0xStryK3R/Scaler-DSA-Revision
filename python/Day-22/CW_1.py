class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ps_arr = [0]
        for num in A:
            if num & 1:
                ps_arr.append(ps_arr[-1] + 1)
            else:
                ps_arr.append(ps_arr[-1] - 1)

        hash_A = {}

        ans = 0

        for i, num in enumerate(ps_arr):
            if num in hash_A:
                ans = max(ans, i - hash_A[num])
            else:
                hash_A[num] = i

        return ans
