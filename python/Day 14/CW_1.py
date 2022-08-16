# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        color_cnt = [0, 0, 0]
        for color in A:
            color_cnt[color] += 1

        return [0]*color_cnt[0] + [1]*color_cnt[1] + [2]*color_cnt[2]
