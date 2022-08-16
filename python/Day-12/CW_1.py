# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        hash_A = {}
        for i, num in enumerate(A):
            if (B - num) in hash_A:
                return [hash_A[B - num] + 1, i + 1]
            hash_A[num] = hash_A.get(num, i)

        return []
