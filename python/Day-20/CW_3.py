# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        N = len(A)
        if B >= N:
            return sum(A)
        ans = sumx = sum(A[:B])
        i = 0
        while(i < B):
            sumx += (A[N-1-i] - A[B-1-i])
            i += 1
            ans = max(ans, sumx)

        return ans
