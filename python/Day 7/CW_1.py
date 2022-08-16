# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


from functools import reduce


class Solution:
    # @param A : list of integers
    # @return an integer
    # Replae Code Here
    def singleNumber(self, A):
        ans = reduce(lambda f, s: f ^ s, A)

        return ans
