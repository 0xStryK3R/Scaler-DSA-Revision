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
        set_a = set()
        cnt = 0
        for num in A:
            if num ^ B in set_a:
                cnt += 1
            set_a.add(num)

        return cnt
