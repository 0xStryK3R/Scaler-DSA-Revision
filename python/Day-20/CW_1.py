# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        ans = [0]*A
        for L, R, P in B:
            ans[L-1] += P
            if R < A:
                ans[R] += - P
        # return ans

        for i in range(1, A):
            ans[i] += ans[i-1]

        return ans
