# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
        B = ''

        for ch in A:
            if -1 < ord(ch)-ord('A') < 26:
                B += chr(ord('a')+ord(ch)-ord('A'))
            else:
                B += ch

        return B
