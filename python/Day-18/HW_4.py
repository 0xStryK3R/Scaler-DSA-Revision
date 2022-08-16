# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        sign = -1 if A < 0 else 1
        A = abs(A)
        B = 0
        while(A):
            B = B*10 + A % 10
            A = int(A/10)

        return 0 if B > 2**31 else B * sign
