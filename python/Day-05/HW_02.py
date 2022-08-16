# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 08:53:28 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A.remove(max(A))
        A.remove(max(A))

        return A
