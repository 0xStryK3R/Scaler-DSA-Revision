# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_upper(self, A):
        B = ''

        for ch in A:
            if -1 < ord(ch)-ord('a') < 26:
                B += chr(ord('A')+ord(ch)-ord('a'))
            else:
                B += ch

        return B
