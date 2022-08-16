# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 09:22:34 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    # Replae Code Here
    def solve(self, A):
        pattern = [[num for num in range(1, i+2)] + [0]*(A-i-1)
                   for i in range(A)]

        return pattern
