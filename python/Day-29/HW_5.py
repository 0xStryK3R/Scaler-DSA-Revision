class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        A += [-1]
        max_sum = -1
        max_sub_arr = []
        cur_sub_arr = []

        for num in A:
            if num < 0:
                if max_sum < sum(cur_sub_arr):
                    max_sub_arr = cur_sub_arr
                    max_sum = sum(cur_sub_arr)
                cur_sub_arr = []
            else:
                cur_sub_arr.append(num)

        return max_sub_arr
