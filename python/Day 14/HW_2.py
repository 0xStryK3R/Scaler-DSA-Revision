# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


def fractional_value(n):
    if n == 0:
        return 0
    x = n
    denom = 1
    while(x):
        x //= 10
        denom *= 10
    denom -= 1
    return n/denom


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        A.sort(key=fractional_value, reverse=True)

        return str(int(''.join(list(map(str, A)))))
