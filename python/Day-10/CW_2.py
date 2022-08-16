# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        for i in range(len(A)):
            for j in range(i+1, len(A[0])):
                A[i][j], A[j][i] = A[j][i], A[i][j]

        for i in range(len(A)):
            A[i] = A[i][::-1]

        return A
