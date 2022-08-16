# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        B = {ch: i for i, ch in enumerate(B)}

        C = sorted(A, key=lambda x: tuple([B[i] for i in x]))

        return int(A == C)
