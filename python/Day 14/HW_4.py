# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        min_cost = 0
        N = len(A)
        for i in range(N):
            min_cost += A[i]*(N-i)
        return min_cost
