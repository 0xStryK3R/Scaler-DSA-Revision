# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if not A:
            return 0
        return A % 10 + self.solve(A//10)
