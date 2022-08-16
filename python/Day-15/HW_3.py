# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq_map = {}
        for ch in A:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        uniq_ch_cnt = len(freq_map.keys())
        a = sorted(freq_map.values())

        i = 0
        freq = a[i]
        i += 1

        for freq in sorted(freq_map.values()):
            if freq < B:
                uniq_ch_cnt -= 1
                B -= freq
            elif B == freq:
                uniq_ch_cnt -= 1
                break
        return uniq_ch_cnt
