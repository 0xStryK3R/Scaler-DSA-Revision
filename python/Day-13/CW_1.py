# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        PS_arr = [0]
        for num in A:
            PS_arr.append(PS_arr[-1] + num)

        hash_ps = {}
        for i, val in enumerate(PS_arr):
            if val-B in hash_ps:
                return A[hash_ps[val-B]:i]
            hash_ps[val] = i

        return [-1]
