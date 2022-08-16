# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 09:12:15 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        even_max = - 10**10
        odd_min = 10**10

        for num in A:
            if num & 1:
                odd_min = min(odd_min, num)
            else:
                even_max = max(even_max, num)

        return even_max - odd_min
