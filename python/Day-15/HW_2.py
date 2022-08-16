# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        cnt = i = 0
        while(i < len(A)-2):
            if A[i:i+3] == 'bob':
                cnt += 1
            i += 1

        return cnt
