# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)
        for i in range(len(A)):
            if i and A[i] == A[i-1]:
                continue
            if A[i] == i:
                return 1
        return -1
