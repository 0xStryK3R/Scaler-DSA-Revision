# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq_map = {}
        for num in A:
            freq_map[num] = freq_map.get(num, 0) + 1

        c = list(freq_map.keys())

        min_val = min(c)
        max_val = max(c)

        min_carry = 0
        max_carry = 0

        while(min_val < max_val and B > 0):
            min_freq = freq_map.get(min_val, 0) + min_carry
            max_freq = freq_map.get(max_val, 0) + max_carry

            if (min_freq <= B and min_freq < max_freq):
                min_val += 1
                min_carry = min_freq
                B -= min_freq
            elif max_freq <= B:
                max_val -= 1
                max_carry = max_freq
                B -= max_freq
            else:
                break

        return max_val - min_val
