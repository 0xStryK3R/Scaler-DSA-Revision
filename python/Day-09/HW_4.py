# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        ans = []
        N = len(A)

        for i in B:
            i %= N
            ans.append(A[i:] + A[:i])

        return ans
