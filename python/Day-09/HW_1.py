# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [https://github.com/0xStryK3R]
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        for i in range(len(A)-1, -1, -1):
            if A[i] == 9:
                A[i] = 0
                if i == 0:
                    A = [1] + A
            else:
                A[i] += 1
                break

        while(A and A[0] == 0):
            A = A[1:]

        return A
