# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        MOD = 10003
        N = len(A)

        cnt = 0

        for i, ch in enumerate(A):
            if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
                cnt += N - i

        return cnt % MOD
