# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        res = []
        for i in range(A):
            row = [0]*A
            for j in range(1, i+2):
                row[j-1] = j
            res.append(row[::-1])

        return res
