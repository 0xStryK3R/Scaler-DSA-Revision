# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A += '0'
        cur_len = prev_len = 0
        zero_count = 0

        group_cnt = 0

        ans = 0
        max_len = 0

        for i in A:
            if i == '1':
                cur_len += 1
                zero_count = 0
                max_len = max(max_len, cur_len)
            else:
                if zero_count:
                    prev_len = 0
                else:
                    if cur_len:
                        group_cnt += 1
                        ans = max(ans, cur_len + 1 + prev_len)
                    zero_count += 1
                    prev_len = cur_len
                    cur_len = 0
            #print(i, prev_len, cur_len, max_len, ans, group_cnt)

        if group_cnt == 2:
            if ans > max_len + 1:
                ans -= 1
            else:
                ans = max_len + 1
        elif group_cnt == 1:
            ans = max_len

        return ans
