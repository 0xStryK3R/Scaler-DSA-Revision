# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return an integer
    # Replae Code Here
    def numSetBits(self, A):
        counter = 0
        while(A):
            A = A & (A-1)
            counter += 1

        return counter
