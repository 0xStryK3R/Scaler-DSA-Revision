# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        P = A[0]
        for word in A:
            P = P[:len(word)]
            word = word[:len(P)]
            for i in range(len(P)):
                if P[i] != word[i]:
                    P = P[:i]
                    break

        return P
