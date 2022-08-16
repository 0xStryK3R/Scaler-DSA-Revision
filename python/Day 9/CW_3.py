# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = ans = len(A)
        i = 0
        while(i+1 < N):
            if A[i] & 1 == A[i+1] & 1:
                ans -= 1
            i += 1

        return ans
