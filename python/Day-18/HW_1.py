# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        col = ''
        while(A):
            A -= 1
            col = chr(ord('A') + A % 26) + col
            A = (int)(A/26)

        return col
