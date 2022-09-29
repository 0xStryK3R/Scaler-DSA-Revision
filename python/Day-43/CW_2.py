class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        ps_map = set([0])
        sum_val = 0
        for num in A:
            sum_val += num
            if sum_val in ps_map:
                return 1
            ps_map.add(sum_val)

        return 0
