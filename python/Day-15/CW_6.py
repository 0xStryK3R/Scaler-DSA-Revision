# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of characters
    # @return an integer
    def solve(self, A):

        for ch in A:
            if not (-1 < ord(ch)-ord('a') < 26 or -1 < ord(ch)-ord('A') < 26 or -1 < ord(ch)-ord('0') < 10):
                return 0

        return 1
