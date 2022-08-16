# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        if len(A) == 1:
            return A
        B = A.copy()
        B[0] = A[0]*A[1]
        B[-1] = B[-1]*B[-2]

        for i in range(1, len(A)-1):
            B[i] = A[i-1]*A[i+1]

        return B
