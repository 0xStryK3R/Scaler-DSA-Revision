# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return an integer
    def findAthFibonacci(self, A):
        if A < 2:
            return A
        return self.findAthFibonacci(A-1) + self.findAthFibonacci(A-2)
