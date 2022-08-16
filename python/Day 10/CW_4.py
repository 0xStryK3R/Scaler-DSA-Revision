# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A < 1:
            return []

        pascal_tri = []

        for i in range(A):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pascal_tri[-1][j]+pascal_tri[-1][j-1])
            for j in range(i+1, A):
                row.append(0)
            pascal_tri.append(row)
        return pascal_tri
