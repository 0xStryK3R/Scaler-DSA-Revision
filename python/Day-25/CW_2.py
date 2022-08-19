class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        ps_arr = [0]
        for bit in A:
            ps_arr.append(ps_arr[-1] + bit)

        ans = []
        
        for l, r in B:
            one_count = ps_arr[r] - ps_arr[l-1]
            xor_val = int(one_count&1)
            zero_count = r - l + 1 - one_count
            ans.append([xor_val, zero_count])
        
        return ans