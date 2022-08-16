# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""
import sys
sys.setrecursionlimit(10**6)


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A, st=0, end=None):
        if end == None:
            end = len(A) - 1

        if end <= st:
            return 1

        if A[st] != A[end]:
            return 0

        return self.solve(A, st+1, end-1)
