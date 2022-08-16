# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        r = len(A[0]) - 1
        for i, row in enumerate(A):
            while(r > -1 and row[r]):
                r -= 1
                ans = i

        return ans
