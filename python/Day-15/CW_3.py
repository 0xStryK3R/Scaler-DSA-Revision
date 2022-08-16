# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        B %= len(A)
        return ''.join(A[-B:] + A[:-B])
