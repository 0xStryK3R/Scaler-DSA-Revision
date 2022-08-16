# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        MOD = 10**9 + 7
        A += 1
        cnt = 0
        i = 2
        while(A << 1 > i):
            complete_cycles = (A//i)
            complete_cycle_bits = complete_cycles * (i >> 1)

            cnt += complete_cycle_bits

            remainder = (A % i) - (i >> 1)
            if remainder < 0:
                remainder = 0

            cnt += remainder

            i = i << 1

        return cnt % MOD
