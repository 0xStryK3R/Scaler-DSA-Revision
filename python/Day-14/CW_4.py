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
        d = (A[-1] - A[0])//(len(A) - 1)
        for i in range(1, len(A)):
            if A[i] - A[i-1] != d:
                return 0
        return 1
