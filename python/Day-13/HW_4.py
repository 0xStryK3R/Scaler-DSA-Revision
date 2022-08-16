# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:20:35 2022

@author: arupb [github.com/0xStryK3R]
"""


class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
    A = str(A)
    prod_set = set()
    N = len(A)
    for i in range(N):
        prod = 1
        for j in range(i, N):
            prod *= int(A[j])
            if prod in prod_set:
                return 0
            prod_set.add(prod)
    return 1
