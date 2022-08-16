# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return a strings
    def getLargest(self, A):
        S, T = A.split('_')
        T = sorted(T, reverse=True)
        new_S = ''
        j = 0
        for ch in S:
            if j < len(T) and ord(ch) < ord(T[j]):
                ch = T[j]
                j += 1
            new_S += ch
        return new_S
