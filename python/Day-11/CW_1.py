# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        MOD = 10**9 + 7
        A = list(A)
        cnt_A = 0
        cnt_AG = 0
        for ch in A:
            if ch == 'A':
                cnt_A += 1
            if ch == 'G':
                cnt_AG += cnt_A

        return cnt_AG % MOD
