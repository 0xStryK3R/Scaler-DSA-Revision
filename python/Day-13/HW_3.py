# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        uniq_A = list(set(A))
        if len(uniq_A) != 2 or A.count(uniq_A[0]) != A.count(uniq_A[1]):
            return 'LOSE'

        return 'WIN'
