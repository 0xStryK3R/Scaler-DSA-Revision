# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        PS_arr = [A[0]]
        for num in A[1:]:
            PS_arr.append(PS_arr[-1] + num)

        ps_set = set()
        for i, val in enumerate(PS_arr):
            if val in ps_set:
                return 1
            ps_set.add(val)
        if 0 in ps_set:
            return 1
        return 0
