# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        N = len(A)
        disparity_cnt = 0
        for i in range(N//2):
            if A[i] != A[N-1-i]:
                disparity_cnt += 1

        if (N & 1 and disparity_cnt < 2) or (disparity_cnt == 1):
            return 'YES'

        return 'NO'
