# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        N = len(A)
        res = []
        for d in range(2*N - 1):
            row = []
            if d < N:
                for i in range(d+1):
                    row.append(A[i][d-i])
            else:
                for i in range(d % N + 1, N):
                    row.append(A[i][d-i])
            row += [0]*(N-len(row))
            res.append(row)
        return res
