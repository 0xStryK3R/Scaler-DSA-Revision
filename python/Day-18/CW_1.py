# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        return sum([((ord(ch) - ord('A') + 1)*26**i) for i, ch in enumerate(A[::-1])])
