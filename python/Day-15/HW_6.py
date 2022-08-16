# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        VOWELS = ('a', 'e', 'i', 'o', 'u')
        B = []
        for i in range(len(A)):
            if -1 < ord(A[i]) - ord('A') < 26:
                continue

            if A[i] in VOWELS:
                B.append('#')
                continue

            B.append(A[i])

        return ''.join(B*2)
