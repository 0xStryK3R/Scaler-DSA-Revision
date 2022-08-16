# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()

        for i in range(0, len(A) - 1, 2):
            A[i], A[i+1] = A[i+1], A[i]

        return A
